"""A simple student sign-in screen for an education portal."""

import tkinter as tk
from tkinter import messagebox


BACKGROUND = "#f4f7fb"
NAVY = "#580202"
BLUE = "#020B1F"
TEXT = "#1c2b43"
MUTED = "#718096"
FIELD = "#ffffff"


class StudentLoginApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Student Portal | Sign in")
        self.root.geometry("1000x660")
        self.root.minsize(800, 560)
        self.root.configure(bg=BACKGROUND)

        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.show_password = tk.BooleanVar(value=False)
        self.notice = tk.StringVar()

        self._build_layout()
        self.root.bind("<Return>", self._submit)

    def _build_layout(self) -> None:
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, minsize=360, weight=4)
        self.root.grid_columnconfigure(1, weight=6)

        self._build_welcome_panel()
        self._build_form_panel()

    def _build_welcome_panel(self) -> None:
        panel = tk.Frame(self.root, bg=NAVY, padx=42, pady=38)
        panel.grid(row=0, column=0, sticky="nsew")
        panel.grid_rowconfigure(2, weight=1)

        brand = tk.Frame(panel, bg=NAVY)
        brand.grid(row=0, column=0, sticky="w")
        tk.Label(
            brand,
            text="✦",
            font=("Segoe UI", 19, "bold"),
            fg="#89aaff",
            bg=NAVY,
        ).pack(side="left", padx=(0, 10))
        tk.Label(
            brand,
            text="LEARNWELL",
            font=("Segoe UI", 12, "bold"),
            fg="white",
            bg=NAVY,
        ).pack(side="left")

        tk.Label(
            panel,
            text="Your next chapter\nstarts here.",
            font=("Segoe UI", 30, "bold"),
            fg="white",
            bg=NAVY,
            justify="left",
            anchor="w",
        ).grid(row=1, column=0, sticky="w", pady=(82, 16))
        tk.Label(
            panel,
            text="A space to learn, grow, and keep track\nof everything happening at school.",
            font=("Segoe UI", 11),
            fg="#c2cde0",
            bg=NAVY,
            justify="left",
            anchor="w",
        ).grid(row=2, column=0, sticky="nw")

        illustration = tk.Canvas(
            panel, bg=NAVY, highlightthickness=0, height=180
        )
        illustration.grid(row=3, column=0, sticky="ew", pady=(8, 0))
        illustration.bind("<Configure>", self._draw_illustration)

        tk.Label(
            panel,
            text="LEARN  ·  CONNECT  ·  ACHIEVE",
            font=("Segoe UI", 8, "bold"),
            fg="#92a5c4",
            bg=NAVY,
        ).grid(row=4, column=0, sticky="w", pady=(20, 0))

    @staticmethod
    def _draw_illustration(event: tk.Event) -> None:
        canvas = event.widget
        canvas.delete("all")
        width = canvas.winfo_width()
        canvas.create_oval(
            width - 190, 18, width - 16, 192, fill="#20395f", outline=""
        )
        canvas.create_oval(
            width - 142, 42, width - 48, 136, fill="#356ae6", outline=""
        )
        canvas.create_oval(
            width - 112, 67, width - 78, 101, fill="#9db7ff", outline=""
        )
        canvas.create_line(
            width - 223, 142, width - 36, 142, fill="#56719a", width=2
        )
        canvas.create_rectangle(
            width - 204, 148, width - 56, 160, fill="#20395f", outline=""
        )

    def _build_form_panel(self) -> None:
        panel = tk.Frame(self.root, bg=BACKGROUND, padx=48, pady=34)
        panel.grid(row=0, column=1, sticky="nsew")

        form = tk.Frame(panel, bg=BACKGROUND, width=390)
        form.place(relx=0.5, rely=0.5, anchor="center")
        form.grid_columnconfigure(0, weight=1)

        tk.Label(
            form,
            text="Welcome back",
            font=("Segoe UI", 25, "bold"),
            fg=TEXT,
            bg=BACKGROUND,
        ).grid(row=0, column=0, sticky="w")
        tk.Label(
            form,
            text="Sign in to your student account to continue.",
            font=("Segoe UI", 10),
            fg=MUTED,
            bg=BACKGROUND,
        ).grid(row=1, column=0, sticky="w", pady=(7, 28))

        self._field_label(form, "Student email or ID", 2)
        self.email_entry = self._entry(form, self.email, 3)
        self.email_entry.bind("<Return>", lambda _event: self.password_entry.focus_set())

        self._field_label(form, "Password", 4)
        self.password_entry = self._entry(form, self.password, 5, show="•")
        self.password_entry.bind("<Return>", self._submit)

        options = tk.Frame(form, bg=BACKGROUND)
        options.grid(row=6, column=0, sticky="ew", pady=(11, 0))
        tk.Checkbutton(
            options,
            text="Show password",
            variable=self.show_password,
            command=self._toggle_password,
            font=("Segoe UI", 9),
            fg=MUTED,
            bg=BACKGROUND,
            activebackground=BACKGROUND,
            selectcolor=BACKGROUND,
            cursor="hand2",
        ).pack(side="left")
        tk.Checkbutton(
            options,
            text="Remember me",
            font=("Segoe UI", 9),
            fg=MUTED,
            bg=BACKGROUND,
            activebackground=BACKGROUND,
            selectcolor=BACKGROUND,
            cursor="hand2",
        ).pack(side="right")

        tk.Button(
            form,
            text="Sign in",
            command=self._submit,
            font=("Segoe UI", 11, "bold"),
            fg="white",
            bg=BLUE,
            activebackground="#2857c5",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            pady=12,
        ).grid(row=7, column=0, sticky="ew", pady=(24, 10))

        tk.Label(
            form,
            textvariable=self.notice,
            font=("Segoe UI", 9),
            fg="#b54747",
            bg=BACKGROUND,
            wraplength=390,
            justify="left",
        ).grid(row=8, column=0, sticky="w")

        footer = tk.Frame(form, bg=BACKGROUND)
        footer.grid(row=9, column=0, sticky="ew", pady=(23, 0))
        tk.Label(
            footer,
            text="Having trouble signing in?",
            font=("Segoe UI", 9),
            fg=MUTED,
            bg=BACKGROUND,
        ).pack(side="left")
        tk.Button(
            footer,
            text="Get help",
            command=self._get_help,
            font=("Segoe UI", 9, "bold"),
            fg=BLUE,
            bg=BACKGROUND,
            activebackground=BACKGROUND,
            activeforeground="#2857c5",
            relief="flat",
            cursor="hand2",
        ).pack(side="left", padx=(5, 0))

        tk.Label(
            form,
            text="For students · Secure school access",
            font=("Segoe UI", 8),
            fg="#9aa5b5",
            bg=BACKGROUND,
        ).grid(row=10, column=0, sticky="w", pady=(32, 0))

    @staticmethod
    def _field_label(parent: tk.Frame, text: str, row: int) -> None:
        tk.Label(
            parent,
            text=text,
            font=("Segoe UI", 9, "bold"),
            fg=TEXT,
            bg=BACKGROUND,
        ).grid(row=row, column=0, sticky="w", pady=(0, 7))

    @staticmethod
    def _entry(
        parent: tk.Frame, variable: tk.StringVar, row: int, show: str = ""
    ) -> tk.Entry:
        border = tk.Frame(parent, bg="#d9e0ea", padx=1, pady=1)
        border.grid(row=row, column=0, sticky="ew", ipady=1, pady=(0, 20))
        entry = tk.Entry(
            border,
            textvariable=variable,
            font=("Segoe UI", 11),
            fg=TEXT,
            bg=FIELD,
            insertbackground=TEXT,
            relief="flat",
            show=show,
        )
        entry.pack(fill="both", ipady=10, padx=10)
        entry.bind(
            "<FocusIn>", lambda _event: border.configure(bg=BLUE)
        )
        entry.bind(
            "<FocusOut>", lambda _event: border.configure(bg="#d9e0ea")
        )
        return entry

    def _toggle_password(self) -> None:
        self.password_entry.configure(show="" if self.show_password.get() else "•")

    def _submit(self, _event: tk.Event | None = None) -> None:
        if not self.email.get().strip() or not self.password.get():
            self.notice.set("Enter your student email or ID and password to continue.")
            if not self.email.get().strip():
                self.email_entry.focus_set()
            else:
                self.password_entry.focus_set()
            return

        self.notice.set("")
        messagebox.showinfo(
            "Sign-in demo",
            "The sign-in screen is ready, but it is not connected to a school "
            "account system yet.",
            parent=self.root,
        )

    def _get_help(self) -> None:
        messagebox.showinfo(
            "Student sign-in help",
            "Please contact your school's IT team or student support desk "
            "for help accessing your account.",
            parent=self.root,
        )


def main() -> None:
    root = tk.Tk()
    StudentLoginApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()