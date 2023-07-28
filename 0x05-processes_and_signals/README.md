# 0x05. Processes and signals :sparkles:
This project is about learning how to manage processes and signals in Linux using Bash scripting 🐚.

- Use man or help to learn more about:
`ps`
`pgrep`
`pkill`
`kill`
`exit`
`trap`

## :bulb: General 
- What is a PID
- What is a process
- How to find a process’ PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored

## :heavy_check_mark: Requirements:
- **All the files will be interpreted on Ubuntu 20.04 LTS 🐧**
- **Bash script must pass Shellcheck (version 0.7.0) without any error ✔️**

## :bust_in_silhouette: Author
[Ahmed Kamal](https://github.com/ahmedmkamal313). 👋

## :file_folder: Files 
The files in this project are:

- [0-what-is-my-pid]: A script that displays its own PID.
- 1-list_your_processes: A script that displays a list of currently running processes.
- [2-show_your_bash_pid]: A script that displays lines containing the word `bash`.
- [3-show_your_bash_pid_made_easy]: A script that displays the PID and process name of processes whose name contain the word `bash`.
- [4-to_infinity_and_beyond]: A script that displays `To infinity and beyond` indefinitely.
- [5-dont_stop_me_now]: A script that stops `4-to_infinity_and_beyond` process.
- [6-stop_me_if_you_can]: A script that stops `4-to_infinity_and_beyond` process without using `kill` or `killall`.
- [7-highlander]: A script that displays:
  - `To infinity` and beyond indefinitely
  - With a `sleep 2` in between each iteration
  - `I am invincible!!!` when receiving a SIGTERM signal
- [8-beheaded_process]: A script that kills the process `7-highlander`.
- [100-process_and_pid_file]: A script that:
  - Creates the file `/var/run/holbertonscript.pid` containing its PID
  - Displays `To infinity and beyond` indefinitely
  - Displays `I hate the kill command` when receiving a SIGTERM signal
  - Deletes the file `/var/run/holbertonscript.pid` and terminates itself when receiving a SIGINT signal
- [101-manage_my_process], [manage_my_process]: Two scripts that:
  - Indicate how to manage my_process using:
    - init.d
    - pidfile
    - log file
    - env file
    - crash log file
  - Start my_process when launching
  - Restart my_process when crashing
  - Stop my_process when running stop action
  - Manage my_process across multiple servers using Fabric (upstart)
  - Display logs in real time when running logs action
- [102-zombie.c]: A C program that creates 5 zombie processes.