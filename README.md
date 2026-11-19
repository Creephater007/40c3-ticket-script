# Windows
### Powershell
Testing
```powershell
Invoke-RestMethod -Uri "https://raw.githubusercontent.com/Creephater007/40c3-ticket-script/main/script_testing.ps1" | Invoke-Expression
```
Real
```powershell
Invoke-RestMethod -Uri "https://raw.githubusercontent.com/Creephater007/40c3-ticket-script/main/script.ps1" | Invoke-Expression
```

### Batch
Testing
```
curl -L "https://raw.githubusercontent.com/Creephater007/40c3-ticket-script/main/script_testing.ps1" | powershell
```
Real
```
curl -L "https://raw.githubusercontent.com/Creephater007/40c3-ticket-script/main/script.ps1" | powershell
```

# Linux
### Bash
Testing
```bash
curl -L "https://raw.githubusercontent.com/Creephater007/40c3-ticket-script/main/script_testing.sh" | sh
```
Real
```bash
curl -L "https://raw.githubusercontent.com/Creephater007/40c3-ticket-script/main/script.sh" | sh
```

# Mac
```zsh
(coming soon)
```
