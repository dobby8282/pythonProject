import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter import filedialog
import sv_ttk
import re
import time
import threading


class SQLExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SQL Query Extractor")
        self.root.geometry("1200x800")

        # Apply sun valley theme
        sv_ttk.set_theme("dark")

        # Make root window responsive
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.create_widgets()

    def create_widgets(self):
        # Create main frame
        main_frame = ttk.Frame(self.root)
        main_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # Create buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        # Create buttons
        ttk.Button(button_frame, text="Open Log File", command=self.open_file).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Extract SQL", command=self.start_extraction).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_all).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Toggle Theme", command=self.toggle_theme).pack(side="left", padx=5)

        # Create progress bar (hidden by default)
        self.progress_var = tk.DoubleVar()
        self.progress = ttk.Progressbar(button_frame, length=200, mode='indeterminate',
                                        variable=self.progress_var)
        self.progress.pack(side="left", padx=20)

        # Create status label
        self.status_label = ttk.Label(button_frame, text="")
        self.status_label.pack(side="left", padx=5)

        # Create input text area
        input_frame = ttk.LabelFrame(main_frame, text="Log Content")
        input_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 5))
        input_frame.grid_rowconfigure(0, weight=1)
        input_frame.grid_columnconfigure(0, weight=1)

        self.input_text = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD)
        self.input_text.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Create output text area with tabs
        output_frame = ttk.LabelFrame(main_frame, text="Extracted SQL")
        output_frame.grid(row=1, column=1, sticky="nsew", padx=(5, 0))
        output_frame.grid_rowconfigure(0, weight=1)
        output_frame.grid_columnconfigure(0, weight=1)

        # Create notebook for tabs
        self.notebook = ttk.Notebook(output_frame)
        self.notebook.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Create tabs with scrolled text that fills the space
        self.param_tab = scrolledtext.ScrolledText(self.notebook, wrap=tk.WORD)
        self.executable_tab = scrolledtext.ScrolledText(self.notebook, wrap=tk.WORD)

        self.notebook.add(self.param_tab, text="With Parameters")
        self.notebook.add(self.executable_tab, text="Executable SQL")

    def start_extraction(self):
        # Disable the extract button and show progress
        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.Button):
                widget.configure(state='disabled')

        self.progress.start(10)
        self.status_label.configure(text="Extracting SQL...")

        # Start extraction in a separate thread
        thread = threading.Thread(target=self.extract_sql)
        thread.daemon = True
        thread.start()

    def finish_extraction(self):
        # Re-enable buttons and hide progress
        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.Button):
                widget.configure(state='normal')

        self.progress.stop()
        self.status_label.configure(text="Extraction completed")

        # Schedule status clear
        self.root.after(3000, lambda: self.status_label.configure(text=""))

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("Log files", "*.log"), ("All files", "*.*")]
        )
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.input_text.delete('1.0', tk.END)
                self.input_text.insert('1.0', file.read())

    def extract_sql(self):
        log_content = self.input_text.get('1.0', tk.END)

        # Clear previous output
        self.param_tab.delete('1.0', tk.END)
        self.executable_tab.delete('1.0', tk.END)

        # Find SQL queries and parameters
        queries = self.extract_queries_and_parameters(log_content)

        # Display formatted results
        for i, (query, params) in enumerate(queries, 1):
            # Simulate some processing time for demonstration
            time.sleep(0.1)

            # Display query with parameters
            self.param_tab.insert(tk.END, f"--- Query #{i} ---\n")
            self.param_tab.insert(tk.END, f"SQL:\n{query}\n")
            if params:
                self.param_tab.insert(tk.END, f"Parameters: {params}\n")
            self.param_tab.insert(tk.END, "\n")

            # Display executable query
            self.executable_tab.insert(tk.END, f"--- Query #{i} ---\n")
            executable_query = self.create_executable_query(query, params)
            self.executable_tab.insert(tk.END, f"{executable_query}\n\n")

        # Schedule completion in main thread
        self.root.after(0, self.finish_extraction)

    def extract_queries_and_parameters(self, log_content):
        results = []

        # Pattern to match "Preparing:" followed by SQL
        prep_pattern = r"Preparing: (.*?)(?=Parameters:|$|\n\d)"
        # Pattern to match "Parameters:" followed by parameter values
        param_pattern = r"Parameters: (.*?)(?=\n\d|$)"

        # Find all SQL queries
        queries = re.finditer(prep_pattern, log_content, re.DOTALL)
        parameters = re.finditer(param_pattern, log_content, re.DOTALL)

        # Convert iterators to lists
        query_list = [(m.start(), m.group(1).strip()) for m in queries]
        param_list = [(m.start(), m.group(1).strip()) for m in parameters]

        # Match queries with their parameters based on position in text
        i = 0
        j = 0
        while i < len(query_list) and j < len(param_list):
            query_pos, query = query_list[i]
            param_pos, params = param_list[j]

            if param_pos > query_pos:
                results.append((query, params))
                i += 1
                j += 1
            else:
                j += 1

        # Add remaining queries without parameters
        while i < len(query_list):
            results.append((query_list[i][1], None))
            i += 1

        return results

    def create_executable_query(self, query, params):
        if not params:
            return query.strip() + ";"

        # Parse parameters
        param_list = []
        current_param = ""
        in_string = False

        for char in params:
            if char == ',' and not in_string:
                if current_param.strip():
                    param_list.append(current_param.strip())
                current_param = ""
            else:
                if char == "'":
                    in_string = not in_string
                current_param += char

        if current_param.strip():
            param_list.append(current_param.strip())

        # Replace question marks with parameter values
        executable_query = query
        for param in param_list:
            # Check if parameter is a string (ends with (String))
            is_string = "(String)" in param
            param = param.replace("(String)", "").strip()

            # Handle null values
            if param.lower() == "null":
                replacement = "NULL"
            # Handle string values
            elif is_string:
                replacement = f"'{param}'"
            # Handle numeric values
            else:
                replacement = param

            # Replace first occurrence of ?
            executable_query = executable_query.replace("?", replacement, 1)

        return executable_query.strip() + ";"

    def clear_all(self):
        self.input_text.delete('1.0', tk.END)
        self.param_tab.delete('1.0', tk.END)
        self.executable_tab.delete('1.0', tk.END)

    def toggle_theme(self):
        current_theme = sv_ttk.get_theme()
        if current_theme == "dark":
            sv_ttk.set_theme("light")
        else:
            sv_ttk.set_theme("dark")


def main():
    root = tk.Tk()
    app = SQLExtractorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()