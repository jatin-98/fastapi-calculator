const input = document.getElementById("expression-input");
const btn = document.getElementById("calculate-btn");
const btnText = document.getElementById("btn-text");
const resultBox = document.getElementById("result-box");
const resultValue = document.getElementById("result-value");
const resultLabel = document.getElementById("result-label");
const themeToggle = document.getElementById("theme-toggle");
const themeIcon = document.getElementById("theme-icon");
const themeLabel = document.getElementById("theme-label");
const html = document.documentElement;

// ── Theme persistence ──
const savedTheme = localStorage.getItem("theme") || "dark";
applyTheme(savedTheme);

themeToggle.addEventListener("click", () => {
    const current = html.getAttribute("data-theme");
    applyTheme(current === "dark" ? "light" : "dark");
});

function applyTheme(theme) {
    html.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
    if (theme === "dark") {
        themeIcon.textContent = "☀️";
        themeLabel.textContent = "Light Mode";
    } else {
        themeIcon.textContent = "🌙";
        themeLabel.textContent = "Dark Mode";
    }
}

// ── Example chips ──
document.getElementById("examples").addEventListener("click", (e) => {
    if (e.target.classList.contains("example-chip")) {
        input.value = e.target.dataset.expr;
        input.focus();
    }
});

// ── Keyboard shortcut ──
input.addEventListener("keydown", (e) => {
    if (e.key === "Enter") calculate();
});

btn.addEventListener("click", calculate);

async function calculate() {
    const expression = input.value.trim();
    if (!expression) {
        showError("Please enter an expression first.");
        return;
    }

    btn.classList.add("loading");
    btnText.textContent = "Calculating…";

    try {
        const response = await fetch("/api/v1/calculator/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ expression }),
        });

        const data = await response.json();

        if (response.ok) {
            showSuccess(data.result);
        } else {
            showError(data.detail || "An unexpected error occurred.");
        }
    } catch (err) {
        showError("Could not connect to the server. Is it running?");
    } finally {
        btn.classList.remove("loading");
        btnText.textContent = "Calculate";
    }
}

function showSuccess(value) {
    resultBox.className = "success";
    resultLabel.textContent = "Result";
    resultValue.textContent = value;
    resultBox.style.display = "block";
}

function showError(message) {
    resultBox.className = "error";
    resultLabel.textContent = "Error";
    resultValue.textContent = message;
    resultBox.style.display = "block";
}
