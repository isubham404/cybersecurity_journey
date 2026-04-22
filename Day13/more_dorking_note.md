### 🔧 Advanced Dorking Techniques
* **Exclusion:** Use `-` to remove irrelevant results. (e.g., `-site:github.com`)
* **Wildcards:** Use `*` to find subdomains. (e.g., `site:*.edu`)
* **Chaining:** Combining `filetype`, `intitle`, and `intext` for surgical precision.

### 🚩 Practical Discovery Exercise
**Objective:** Identify exposed log files for a mock target.
**Query:** `filetype:log intext:"password failure" "targetname"`
**Logic:** Log files often record failed login attempts, which sometimes inadvertently include the password the user typed by mistake.