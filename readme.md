## Docker Bench for Security

#### Overview
Docker Bench for Security is a script that checks for dozens of common best-practices around deploying Docker containers in production. It provides a convenient way to assess the security configurations of your Docker environment against a set of recommended practices.

#### Features
- Automated checks for Docker security configurations.
- Supports both manual and automated checks.
- Provides a score indicating the security posture of your Docker setup.

#### Installation
1. Clone the Docker Bench for Security repository:
    ```bash
    git clone https://github.com/docker/docker-bench-security.git
    ```

1. Navigate to the cloned directory:
    ```bash
    cd docker-bench-security
    ```

#### Running with Docker
### Building Docker image
You have two options if you wish to build and run this container yourself:

1. Use Docker Build:
    ```bash
    git clone https://github.com/docker/docker-bench-security.git
    cd docker-bench-security
    docker build --no-cache -t docker-bench-security .
    ```

Followed by an appropriate ```bash docker run ``` command.

2. Use Docker Compose:
    ```bash
    git clone https://github.com/docker/docker-bench-security.git
    cd docker-bench-security
    docker-compose run --rm docker-bench-security
    ```


#### Usage
1. Run the Docker Bench for Security script:
    ```bash
    sudo sh docker-bench-security.sh
    ```

2. Optionally, you can redirect the output to a JSON file:
    ```bash
    sudo sh docker-bench-security.sh -l /output-folder/docker-bench_output

    ```

#### Parsing JSON Output to HTML
The original .json appears as follows:
```json
{
  "dockerbenchsecurity": "1.6.0",
  "start": 1711552881,
  "tests": [
    {
      "id": "1",
      "desc": "Host Configuration",
      "results": [
        {
          "id": "1.1.1",
          "desc": "Ensure a separate partition for containers has been created (Automated)",
          "result": "WARN"
        },
        {
          "id": "1.1.2",
          "desc": "Ensure only trusted users are allowed to control Docker daemon (Automated)",
          "result": "INFO",
          "details": "doubtfulusers: kali",
          "items": [
            "kali"
          ]
        },
        {
          "id": "1.1.3",
          "desc": "Ensure auditing is configured for the Docker daemon (Automated)",
          "result": "WARN"
        },
        {
          "id": "1.1.4",
          "desc": "Ensure auditing is configured for Docker files and directories -/run/containerd (Automated)",
          "result": "WARN"
        },
        {
          "id": "1.1.5",
          "desc": "Ensure auditing is configured for Docker files and directories - /var/lib/docker (Automated)",
          "result": "WARN"
        },
        {
          "id": "1.1.6",
          "desc": "Ensure auditing is configured for Docker files and directories - /etc/docker (Automated)",
          "result": "WARN"
        },
        {
          "id": "1.1.7",
          "desc": "Ensure auditing is configured for Docker files and directories - docker.service (Automated)",
          "result": "WARN"
        },
        {
          "id": "1.1.8",
          "desc": "Ensure auditing is configured for Docker files and directories - containerd.sock (Automated)",
          "result": "INFO",
          "details": "File not found"
        },
        {
          "id": "1.1.9",
          "desc": "Ensure auditing is configured for Docker files and directories - docker.socket (Automated)",
          "result": "WARN"
        },
        {
          "id": "1.1.10",
          "desc": "Ensure auditing is configured for Docker files and directories - /etc/default/docker (Automated)",
          "result": "WARN"
        },
        {
          "id": "1.1.11",
          "desc": "Ensure auditing is configured for Dockerfiles and directories - /etc/docker/daemon.json (Automated)",
          "result": "INFO",
          "details": "File not found"
        },
        {
          "id": "1.1.12",
          "desc": "1.1.12 Ensure auditing is configured for Dockerfiles and directories - /etc/containerd/config.toml (Automated)",
          "result": "WARN"
        },
        {
          "id": "1.1.13",
          "desc": "Ensure auditing is configured for Docker files and directories - /etc/sysconfig/docker (Automated)",
          "result": "INFO",
          "details": "File not found"
        },
        {
          "id": "1.1.14",
          "desc": "Ensure auditing is configured for Docker files and directories - /usr/bin/containerd (Automated)",
          "result": "WARN"
        },
        {
          "id": "1.1.15",
          "desc": "Ensure auditing is configured for Docker files and directories - /usr/bin/containerd-shim (Automated)",
          "result": "WARN"
        },
        {
          "id": "1.1.16",
          "desc": "Ensure auditing is configured for Docker files and directories - /usr/bin/containerd-shim-runc-v1 (Automated)",
          "result": "WARN"
        },
        {
          "id": "1.1.17",
          "desc": "Ensure auditing is configured for Docker files and directories - /usr/bin/containerd-shim-runc-v2 (Automated)",
          "result": "WARN"
        },
        {
          "id": "1.1.18",
          "desc": "Ensure auditing is configured for Docker files and directories - /usr/bin/runc (Automated)",
          "result": "WARN"
        },
        {
          "id": "1.2.1",
          "desc": "Ensure the container host has been Hardened (Manual)",
          "result": "INFO"
        },
        {
          "id": "1.2.2",
          "desc": "Ensure that the version of Docker is up to date (Manual)",
          "result": "INFO",
          "details": "Using 20.10.25+1"
        }
      ]
    },
    {
      "id": "2",
      "desc": "Docker daemon configuration",
      "results": [
        {
          "id": "2.1",
          "desc": "Run the Docker daemon as a non-root user, if possible (Manual)",
          "result": "INFO"
        },
        {
          "id": "2.2",
          "desc": "Ensure network traffic is restricted between containers on the default bridge (Scored)",
          "result": "WARN"
        },
        {
          "id": "2.3",
          "desc": "Ensure the logging level is set to 'info' (Scored)",
          "result": "PASS"
        },
        {
          "id": "2.4",
          "desc": "Ensure Docker is allowed to make changes to iptables (Scored)",
          "result": "PASS"
        },
        {
          "id": "2.5",
          "desc": "Ensure insecure registries are not used (Scored)",
          "result": "PASS"
        },
        {
          "id": "2.6",
          "desc": "Ensure aufs storage driver is not used (Scored)",
          "result": "PASS"
        },
        {
          "id": "2.7",
          "desc": "Ensure TLS authentication for Docker daemon is configured (Scored)",
          "result": "INFO",
          "details": "Docker daemon not listening on TCP"
        },
        {
          "id": "2.8",
          "desc": "Ensure the default ulimit is configured appropriately (Manual)",
          "result": "INFO",
          "details": "Default ulimit doesn't appear to be set"
        },
        {
          "id": "2.9",
          "desc": "Enable user namespace support (Scored)",
          "result": "WARN"
        },
        {
          "id": "2.10",
          "desc": "Ensure the default cgroup usage has been confirmed (Scored)",
          "result": "PASS"
        },
        {
          "id": "2.11",
          "desc": "Ensure base device size is not changed until needed (Scored)",
          "result": "PASS"
        },
        {
          "id": "2.12",
          "desc": "Ensure that authorization for Docker client commands is enabled (Scored)",
          "result": "WARN"
        },
        {
          "id": "2.13",
          "desc": "Ensure centralized and remote logging is configured (Scored)",
          "result": "WARN"
        },
        {
          "id": "2.14",
          "desc": "Ensure containers are restricted from acquiring new privileges (Scored)",
          "result": "WARN"
        },
        {
          "id": "2.15",
          "desc": "Ensure live restore is enabled (Scored)",
          "result": "WARN"
        },
        {
          "id": "2.16",
          "desc": "Ensure Userland Proxy is Disabled (Scored)",
          "result": "WARN"
        },
        {
          "id": "2.17",
          "desc": "Ensure that a daemon-wide custom seccomp profile is applied if appropriate (Manual)",
          "result": "PASS"
        },
        {
          "id": "2.18",
          "desc": "Ensure that experimental features are not implemented in production (Scored)",
          "result": "INFO"
        }
      ]
    },
    {
      "id": "3",
      "desc": "Docker daemon configuration files",
      "results": [
        {
          "id": "3.1",
          "desc": "Ensure that the docker.service file ownership is set to root:root (Automated)",
          "result": "PASS"
        },
        {
          "id": "3.2",
          "desc": "Ensure that docker.service file permissions are appropriately set (Automated)",
          "result": "PASS"
        },
        {
          "id": "3.3",
          "desc": "Ensure that docker.socket file ownership is set to root:root (Automated)",
          "result": "PASS"
        },
        {
          "id": "3.4",
          "desc": "Ensure that docker.socket file permissions are set to 644 or more restrictive (Automated)",
          "result": "PASS"
        },
        {
          "id": "3.5",
          "desc": "Ensure that the /etc/docker directory ownership is set to root:root (Automated)",
          "result": "PASS"
        },
        {
          "id": "3.6",
          "desc": "Ensure that /etc/docker directory permissions are set to 755 or more restrictively (Automated)",
          "result": "PASS"
        },
        {
          "id": "3.7",
          "desc": "Ensure that registry certificate file ownership is set to root:root (Automated)",
          "result": "INFO",
          "details": "Directory not found"
        },
        {
          "id": "3.8",
          "desc": "Ensure that registry certificate file permissions are set to 444 or more restrictively (Automated)",
          "result": "INFO",
          "details": "Directory not found"
        },
        {
          "id": "3.9",
          "desc": "Ensure that TLS CA certificate file ownership is set to root:root (Automated)",
          "result": "INFO",
          "details": "No TLS CA certificate found"
        },
        {
          "id": "3.10",
          "desc": "Ensure that TLS CA certificate file permissions are set to 444 or more restrictively (Automated)",
          "result": "INFO",
          "details": "No TLS CA certificate found"
        },
        {
          "id": "3.11",
          "desc": "Ensure that Docker server certificate file ownership is set to root:root (Automated)",
          "result": "INFO",
          "details": "No TLS Server certificate found"
        },
        {
          "id": "3.12",
          "desc": "Ensure that the Docker server certificate file permissions are set to 444 or more restrictively (Automated)",
          "result": "INFO",
          "details": "No TLS Server certificate found"
        },
        {
          "id": "3.13",
          "desc": "Ensure that the Docker server certificate key file ownership is set to root:root (Automated)",
          "result": "INFO",
          "details": "No TLS Key found"
        },
        {
          "id": "3.14",
          "desc": "Ensure that the Docker server certificate key file permissions are set to 400 (Automated)",
          "result": "INFO",
          "details": "No TLS Key found"
        },
        {
          "id": "3.15",
          "desc": "Ensure that the Docker socket file ownership is set to root:docker (Automated)",
          "result": "PASS"
        },
        {
          "id": "3.16",
          "desc": "Ensure that the Docker socket file permissions are set to 660 or more restrictively (Automated)",
          "result": "PASS"
        },
        {
          "id": "3.17",
          "desc": "Ensure that the daemon.json file ownership is set to root:root (Automated)",
          "result": "INFO",
          "details": "File not found"
        },
        {
          "id": "3.18",
          "desc": "Ensure that daemon.json file permissions are set to 644 or more restrictive (Automated)",
          "result": "INFO",
          "details": "File not found"
        },
        {
          "id": "3.19",
          "desc": "Ensure that the /etc/default/docker file ownership is set to root:root (Automated)",
          "result": "PASS"
        },
        {
          "id": "3.20",
          "desc": "Ensure that the /etc/default/docker file permissions are set to 644 or more restrictively (Automated)",
          "result": "PASS"
        },
        {
          "id": "3.21",
          "desc": "Ensure that the /etc/sysconfig/docker file permissions are set to 644 or more restrictively (Automated)",
          "result": "INFO",
          "details": "File not found"
        },
        {
          "id": "3.22",
          "desc": "Ensure that the /etc/sysconfig/docker file ownership is set to root:root (Automated)",
          "result": "INFO",
          "details": "File not found"
        },
        {
          "id": "3.23",
          "desc": "Ensure that the Containerd socket file ownership is set to root:root (Automated)",
          "result": "PASS"
        },
        {
          "id": "3.24",
          "desc": "Ensure that the Containerd socket file permissions are set to 660 or more restrictively (Automated)",
          "result": "PASS"
        }
      ]
    },
    {
      "id": "4",
      "desc": "Container Images and Build File",
      "results": [
        {
          "id": "4.1",
          "desc": "Ensure that a user for the container has been created (Automated)",
          "result": "WARN",
          "details": "running as root:  reverent_noyce nice_blackburn",
          "items": [
            "reverent_noyce","nice_blackburn"
          ]
        },
        {
          "id": "4.2",
          "desc": "Ensure that containers use only trusted base images (Manual)",
          "result": "NOTE"
        },
        {
          "id": "4.3",
          "desc": "Ensure that unnecessary packages are not installed in the container (Manual)",
          "result": "NOTE"
        },
        {
          "id": "4.4",
          "desc": "Ensure images are scanned and rebuilt to include security patches (Manual)",
          "result": "NOTE"
        },
        {
          "id": "4.5",
          "desc": "Ensure Content trust for Docker is Enabled (Automated)",
          "result": "WARN"
        },
        {
          "id": "4.6",
          "desc": "Ensure that HEALTHCHECK instructions have been added to container images (Automated)",
          "result": "WARN",
          "details": "Images w/o HEALTHCHECK:  [docker:latest] [ubuntu:latest] [python:latest] [ghcr.io/osgeo/gdal:ubuntu-full-latest] [alpine:latest] 8ca4688f4f35 [hello-world:latest]",
          "items": [
            "[docker:latest]","[ubuntu:latest]","[python:latest]","[ghcr.io/osgeo/gdal:ubuntu-full-latest]","[alpine:latest]","8ca4688f4f35","[hello-world:latest]"
          ]
        },
        {
          "id": "4.7",
          "desc": "Ensure update instructions are not used alone in the Dockerfile (Manual)",
          "result": "INFO",
          "details": "Update instructions found:  [python:latest]",
          "items": [
            "[python:latest]"
          ]
        },
        {
          "id": "4.8",
          "desc": "Ensure setuid and setgid permissions are removed (Manual)",
          "result": "NOTE"
        },
        {
          "id": "4.9",
          "desc": "Ensure that COPY is used instead of ADD in Dockerfiles (Manual)",
          "result": "INFO",
          "details": "Images using ADD:  [ubuntu:latest] [ghcr.io/osgeo/gdal:ubuntu-full-latest]",
          "items": [
            "[ubuntu:latest]","[ghcr.io/osgeo/gdal:ubuntu-full-latest]"
          ]
        },
        {
          "id": "4.10",
          "desc": "Ensure secrets are not stored in Dockerfiles (Manual)",
          "result": "NOTE"
        },
        {
          "id": "4.11",
          "desc": "Ensure only verified packages are installed (Manual)",
          "result": "NOTE"
        },
        {
          "id": "4.12",
          "desc": "Ensure all signed artifacts are validated (Manual)",
          "result": "NOTE"
        }
      ]
    },
    {
      "id": "5",
      "desc": "Container Runtime",
      "results": [
        {
          "id": "5.1",
          "desc": "Ensure swarm mode is not Enabled, if not needed (Automated)",
          "result": "PASS"
        },
        {
          "id": "5.2",
          "desc": "Ensure that, if applicable, an AppArmor Profile is enabled (Automated)",
          "result": "PASS"
        },
        {
          "id": "5.3",
          "desc": "Ensure that, if applicable, SELinux security options are set (Automated)",
          "result": "WARN",
          "details": "Containers with no SecurityOptions:  reverent_noyce nice_blackburn",
          "items": [
            "reverent_noyce","nice_blackburn"
          ]
        },
        {
          "id": "5.4",
          "desc": "Ensure that Linux kernel capabilities are restricted within containers (Automated)",
          "result": "PASS"
        },
        {
          "id": "5.5",
          "desc": "Ensure that privileged containers are not used (Automated)",
          "result": "PASS"
        },
        {
          "id": "5.6",
          "desc": "Ensure sensitive host system directories are not mounted on containers (Automated)",
          "result": "PASS"
        },
        {
          "id": "5.7",
          "desc": "Ensure sshd is not run within containers (Automated)",
          "result": "PASS"
        },
        {
          "id": "5.8",
          "desc": "Ensure privileged ports are not mapped within containers (Automated)",
          "result": "PASS"
        },
        {
          "id": "5.9",
          "desc": "Ensure that only needed ports are open on the container (Manual)",
          "result": "PASS"
        },
        {
          "id": "5.10",
          "desc": "Ensure that the host's network namespace is not shared (Automated)",
          "result": "PASS"
        },
        {
          "id": "5.11",
          "desc": "Ensure that the memory usage for containers is limited (Automated)",
          "result": "WARN",
          "details": "Container running without memory restrictions:  reverent_noyce nice_blackburn",
          "items": [
            "reverent_noyce","nice_blackburn"
          ]
        },
        {
          "id": "5.12",
          "desc": "Ensure that CPU priority is set appropriately on containers (Automated)",
          "result": "WARN",
          "details": "Containers running without CPU restrictions:  reverent_noyce nice_blackburn",
          "items": [
            "reverent_noyce","nice_blackburn"
          ]
        },
        {
          "id": "5.13",
          "desc": "Ensure that the container's root filesystem is mounted as read only (Automated)",
          "result": "WARN",
          "details": "Containers running with root FS mounted R/W:  reverent_noyce nice_blackburn",
          "items": [
            "reverent_noyce","nice_blackburn"
          ]
        },
        {
          "id": "5.14",
          "desc": "Ensure that incoming container traffic is bound to a specific host interface (Automated)",
          "result": "PASS"
        },
        {
          "id": "5.15",
          "desc": "Ensure that the 'on-failure' container restart policy is set to '5' (Automated)",
          "result": "PASS"
        },
        {
          "id": "5.16",
          "desc": "Ensure that the host's process namespace is not shared (Automated)",
          "result": "PASS"
        },
        {
          "id": "5.17",
          "desc": "Ensure that the host's IPC namespace is not shared (Automated)",
          "result": "PASS"
        },
        {
          "id": "5.18",
          "desc": "Ensure that host devices are not directly exposed to containers (Manual)",
          "result": "PASS"
        },
        {
          "id": "5.19",
          "desc": "Ensure that the default ulimit is overwritten at runtime if needed (Manual)",
          "result": "INFO",
          "details": "Containers with no default ulimit override:  reverent_noyce nice_blackburn",
          "items": [
            "reverent_noyce","nice_blackburn"
          ]
        },
        {
          "id": "5.20",
          "desc": "Ensure mount propagation mode is not set to shared (Automated)",
          "result": "PASS"
        },
        {
          "id": "5.21",
          "desc": "Ensure that the host's UTS namespace is not shared (Automated)",
          "result": "PASS"
        },
        {
          "id": "5.22",
          "desc": "Ensure the default seccomp profile is not Disabled (Automated)",
          "result": "PASS"
        },
        {
          "id": "5.23",
          "desc": "Ensure that docker exec commands are not used with the privileged option (Automated)",
          "result": "NOTE"
        },
        {
          "id": "5.24",
          "desc": "Ensure that docker exec commands are not used with the user=root option (Manual)",
          "result": "NOTE"
        },
        {
          "id": "5.25",
          "desc": "Ensure that cgroup usage is confirmed (Automated)",
          "result": "PASS"
        },
        {
          "id": "5.26",
          "desc": "Ensure that the container is restricted from acquiring additional privileges (Automated)",
          "result": "WARN",
          "details": "Containers without restricted privileges:  reverent_noyce nice_blackburn",
          "items": [
            "reverent_noyce","nice_blackburn"
          ]
        },
        {
          "id": "5.27",
          "desc": "Ensure that container health is checked at runtime (Automated)",
          "result": "WARN",
          "details": "Containers without health check:  reverent_noyce nice_blackburn",
          "items": [
            "reverent_noyce","nice_blackburn"
          ]
        },
        {
          "id": "5.28",
          "desc": "Ensure that Docker commands always make use of the latest version of their image (Manual)",
          "result": "INFO"
        },
        {
          "id": "5.29",
          "desc": "Ensure that the PIDs cgroup limit is used (Automated)",
          "result": "WARN",
          "details": "Containers without PIDs cgroup limit:  reverent_noyce nice_blackburn",
          "items": [
            "reverent_noyce","nice_blackburn"
          ]
        },
        {
          "id": "5.30",
          "desc": "Ensure that Docker's default bridge 'docker0' is not used (Manual)",
          "result": "INFO",
          "details": "Containers using docker0 network:  3031a689826da0bfe570e50d0752ae08f4230ed94cf14099a4fc46c4e7a10755:reverent_noyce e71ad4feabcef64c1de640af5011b7686502e1dfac69fefa0e7b6f50d2d59cf0:nice_blackburn",
          "items": [
            "3031a689826da0bfe570e50d0752ae08f4230ed94cf14099a4fc46c4e7a10755:reverent_noyce","e71ad4feabcef64c1de640af5011b7686502e1dfac69fefa0e7b6f50d2d59cf0:nice_blackburn"
          ]
        },
        {
          "id": "5.31",
          "desc": "Ensure that the host's user namespaces are not shared (Automated)",
          "result": "PASS"
        },
        {
          "id": "5.32",
          "desc": "Ensure that the Docker socket is not mounted inside any containers (Automated)",
          "result": "PASS"
        }
      ]
    },
    {
      "id": "6",
      "desc": "Docker Security Operations",
      "results": [
        {
          "id": "6.1",
          "desc": "Ensure that image sprawl is avoided (Manual)",
          "result": "INFO",
          "details": "7 active/8 in use"
        },
        {
          "id": "6.2",
          "desc": "Ensure that container sprawl is avoided (Manual)",
          "result": "INFO",
          "details": "7 total/2 running"
        }
      ]
    },
    {
      "id": "7",
      "desc": "Docker Swarm Configuration",
      "results": [
        {
          "id": "7.1",
          "desc": "Ensure that the minimum number of manager nodes have been created in a swarm (Automated)",
          "result": "PASS"
        },
        {
          "id": "7.2",
          "desc": "Ensure that swarm services are bound to a specific host interface (Automated)",
          "result": "PASS"
        },
        {
          "id": "7.3",
          "desc": "Ensure that all Docker swarm overlay networks are encrypted (Automated)",
          "result": "PASS"
        },
        {
          "id": "7.4",
          "desc": "Ensure that Docker's secret management commands are used for managing secrets in a swarm cluster (Manual)",
          "result": "PASS"
        },
        {
          "id": "7.5",
          "desc": "Ensure that swarm manager is run in auto-lock mode (Automated)",
          "result": "PASS"
        },
        {
          "id": "7.6",
          "desc": "Ensure that the swarm manager auto-lock key is rotated periodically (Manual)",
          "result": "PASS"
        },
        {
          "id": "7.7",
          "desc": "Ensure that node certificates are rotated as appropriate (Manual)",
          "result": "PASS"
        },
        {
          "id": "7.8",
          "desc": "Ensure that CA certificates are rotated as appropriate (Manual)",
          "result": "PASS"
        },
        {
          "id": "7.9",
          "desc": "Ensure that management plane traffic is separated from data plane traffic (Manual)",
          "result": "PASS"
        }
      ]
    }
  ],
  "checks": 117,
  "score": 10,
  "end": 1711552886
}
```

To parse the JSON output generated by Docker Bench for Security into an HTML report, you can use a Python script. Here's a simple example of how to do it:

```python
import json

def json2html(input_file, output_file):

    # Aquí va tu código para leer y analizar el JSON desde un archivo o una cadena.

    with open(input_file, 'r') as f:
        data = json.load(f)

    # Generar HTML
    html = "<!DOCTYPE html>\n<html>\n<head>\n<title>Docker Bench Security Report</title>\n</head>\n<body>\n"

    # Agregar información general
    html += "<h1>Docker Bench Security Report</h1>\n"
    html += f"<p>Version: {data['dockerbenchsecurity']}</p>\n"
    html += f"<p>Start Time: {data['start']}</p>\n"
    html += f"<p>End Time: {data['end']}</p>\n"
    html += f"<p>Total Checks: {data['checks']}</p>\n"
    html += f"<p>Score: {data['score']}</p>\n"

    # Agregar resultados de las pruebas
    html += "<h2>Test Results</h2>\n"
    for test in data["tests"]:
        html += f"<h3>{test['desc']}</h3>\n"
        html += "<ul>\n"
        for result in test["results"]:
            html += f"<li>{result['desc']}: {result['result']}</li>\n"
            if "details" in result:
                html += f"<p>{result['details']}</p>\n"
        html += "</ul>\n"

    html += "</body>\n</html>"

    output_name = output_file
    # Guardar el HTML en un archivo
    with open(output_name, "w") as file:
        file.write(html)

    print(f"Se ha generado el archivo HTML: {output_name}")

json2html("docker-bench_output.json", "docker_bench_report.html")


# Generate HTML report (refer to the Python code example provided in previous response)
```html
<!DOCTYPE html>
<html>
<head>
<title>Docker Bench Security Report</title>
</head>
<body>
<h1>Docker Bench Security Report</h1>
<p>Version: 1.6.0</p>
<p>Start Time: 1711552881</p>
<p>End Time: 1711552886</p>
<p>Total Checks: 117</p>
<p>Score: 10</p>
<h2>Test Results</h2>
<h3>Host Configuration</h3>
<ul>
<li>Ensure a separate partition for containers has been created (Automated): WARN</li>
<li>Ensure only trusted users are allowed to control Docker daemon (Automated): INFO</li>
<p>doubtfulusers: kali</p>
<li>Ensure auditing is configured for the Docker daemon (Automated): WARN</li>
<li>Ensure auditing is configured for Docker files and directories -/run/containerd (Automated): WARN</li>
<li>Ensure auditing is configured for Docker files and directories - /var/lib/docker (Automated): WARN</li>
<li>Ensure auditing is configured for Docker files and directories - /etc/docker (Automated): WARN</li>
<li>Ensure auditing is configured for Docker files and directories - docker.service (Automated): WARN</li>
<li>Ensure auditing is configured for Docker files and directories - containerd.sock (Automated): INFO</li>
<p>File not found</p>
<li>Ensure auditing is configured for Docker files and directories - docker.socket (Automated): WARN</li>
<li>Ensure auditing is configured for Docker files and directories - /etc/default/docker (Automated): WARN</li>
<li>Ensure auditing is configured for Dockerfiles and directories - /etc/docker/daemon.json (Automated): INFO</li>
<p>File not found</p>
<li>1.1.12 Ensure auditing is configured for Dockerfiles and directories - /etc/containerd/config.toml (Automated): WARN</li>
<li>Ensure auditing is configured for Docker files and directories - /etc/sysconfig/docker (Automated): INFO</li>
<p>File not found</p>
<li>Ensure auditing is configured for Docker files and directories - /usr/bin/containerd (Automated): WARN</li>
<li>Ensure auditing is configured for Docker files and directories - /usr/bin/containerd-shim (Automated): WARN</li>
<li>Ensure auditing is configured for Docker files and directories - /usr/bin/containerd-shim-runc-v1 (Automated): WARN</li>
<li>Ensure auditing is configured for Docker files and directories - /usr/bin/containerd-shim-runc-v2 (Automated): WARN</li>
<li>Ensure auditing is configured for Docker files and directories - /usr/bin/runc (Automated): WARN</li>
<li>Ensure the container host has been Hardened (Manual): INFO</li>
<li>Ensure that the version of Docker is up to date (Manual): INFO</li>
<p>Using 20.10.25+1</p>
</ul>
<h3>Docker daemon configuration</h3>
<ul>
<li>Run the Docker daemon as a non-root user, if possible (Manual): INFO</li>
<li>Ensure network traffic is restricted between containers on the default bridge (Scored): WARN</li>
<li>Ensure the logging level is set to 'info' (Scored): PASS</li>
<li>Ensure Docker is allowed to make changes to iptables (Scored): PASS</li>
<li>Ensure insecure registries are not used (Scored): PASS</li>
<li>Ensure aufs storage driver is not used (Scored): PASS</li>
<li>Ensure TLS authentication for Docker daemon is configured (Scored): INFO</li>
<p>Docker daemon not listening on TCP</p>
<li>Ensure the default ulimit is configured appropriately (Manual): INFO</li>
<p>Default ulimit doesn't appear to be set</p>
<li>Enable user namespace support (Scored): WARN</li>
<li>Ensure the default cgroup usage has been confirmed (Scored): PASS</li>
<li>Ensure base device size is not changed until needed (Scored): PASS</li>
<li>Ensure that authorization for Docker client commands is enabled (Scored): WARN</li>
<li>Ensure centralized and remote logging is configured (Scored): WARN</li>
<li>Ensure containers are restricted from acquiring new privileges (Scored): WARN</li>
<li>Ensure live restore is enabled (Scored): WARN</li>
<li>Ensure Userland Proxy is Disabled (Scored): WARN</li>
<li>Ensure that a daemon-wide custom seccomp profile is applied if appropriate (Manual): PASS</li>
<li>Ensure that experimental features are not implemented in production (Scored): INFO</li>
</ul>
<h3>Docker daemon configuration files</h3>
<ul>
<li>Ensure that the docker.service file ownership is set to root:root (Automated): PASS</li>
<li>Ensure that docker.service file permissions are appropriately set (Automated): PASS</li>
<li>Ensure that docker.socket file ownership is set to root:root (Automated): PASS</li>
<li>Ensure that docker.socket file permissions are set to 644 or more restrictive (Automated): PASS</li>
<li>Ensure that the /etc/docker directory ownership is set to root:root (Automated): PASS</li>
<li>Ensure that /etc/docker directory permissions are set to 755 or more restrictively (Automated): PASS</li>
<li>Ensure that registry certificate file ownership is set to root:root (Automated): INFO</li>
<p>Directory not found</p>
<li>Ensure that registry certificate file permissions are set to 444 or more restrictively (Automated): INFO</li>
<p>Directory not found</p>
<li>Ensure that TLS CA certificate file ownership is set to root:root (Automated): INFO</li>
<p>No TLS CA certificate found</p>
<li>Ensure that TLS CA certificate file permissions are set to 444 or more restrictively (Automated): INFO</li>
<p>No TLS CA certificate found</p>
<li>Ensure that Docker server certificate file ownership is set to root:root (Automated): INFO</li>
<p>No TLS Server certificate found</p>
<li>Ensure that the Docker server certificate file permissions are set to 444 or more restrictively (Automated): INFO</li>
<p>No TLS Server certificate found</p>
<li>Ensure that the Docker server certificate key file ownership is set to root:root (Automated): INFO</li>
<p>No TLS Key found</p>
<li>Ensure that the Docker server certificate key file permissions are set to 400 (Automated): INFO</li>
<p>No TLS Key found</p>
<li>Ensure that the Docker socket file ownership is set to root:docker (Automated): PASS</li>
<li>Ensure that the Docker socket file permissions are set to 660 or more restrictively (Automated): PASS</li>
<li>Ensure that the daemon.json file ownership is set to root:root (Automated): INFO</li>
<p>File not found</p>
<li>Ensure that daemon.json file permissions are set to 644 or more restrictive (Automated): INFO</li>
<p>File not found</p>
<li>Ensure that the /etc/default/docker file ownership is set to root:root (Automated): PASS</li>
<li>Ensure that the /etc/default/docker file permissions are set to 644 or more restrictively (Automated): PASS</li>
<li>Ensure that the /etc/sysconfig/docker file permissions are set to 644 or more restrictively (Automated): INFO</li>
<p>File not found</p>
<li>Ensure that the /etc/sysconfig/docker file ownership is set to root:root (Automated): INFO</li>
<p>File not found</p>
<li>Ensure that the Containerd socket file ownership is set to root:root (Automated): PASS</li>
<li>Ensure that the Containerd socket file permissions are set to 660 or more restrictively (Automated): PASS</li>
</ul>
<h3>Container Images and Build File</h3>
<ul>
<li>Ensure that a user for the container has been created (Automated): WARN</li>
<p>running as root:  reverent_noyce nice_blackburn</p>
<li>Ensure that containers use only trusted base images (Manual): NOTE</li>
<li>Ensure that unnecessary packages are not installed in the container (Manual): NOTE</li>
<li>Ensure images are scanned and rebuilt to include security patches (Manual): NOTE</li>
<li>Ensure Content trust for Docker is Enabled (Automated): WARN</li>
<li>Ensure that HEALTHCHECK instructions have been added to container images (Automated): WARN</li>
<p>Images w/o HEALTHCHECK:  [docker:latest] [ubuntu:latest] [python:latest] [ghcr.io/osgeo/gdal:ubuntu-full-latest] [alpine:latest] 8ca4688f4f35 [hello-world:latest]</p>
<li>Ensure update instructions are not used alone in the Dockerfile (Manual): INFO</li>
<p>Update instructions found:  [python:latest]</p>
<li>Ensure setuid and setgid permissions are removed (Manual): NOTE</li>
<li>Ensure that COPY is used instead of ADD in Dockerfiles (Manual): INFO</li>
<p>Images using ADD:  [ubuntu:latest] [ghcr.io/osgeo/gdal:ubuntu-full-latest]</p>
<li>Ensure secrets are not stored in Dockerfiles (Manual): NOTE</li>
<li>Ensure only verified packages are installed (Manual): NOTE</li>
<li>Ensure all signed artifacts are validated (Manual): NOTE</li>
</ul>
<h3>Container Runtime</h3>
<ul>
<li>Ensure swarm mode is not Enabled, if not needed (Automated): PASS</li>
<li>Ensure that, if applicable, an AppArmor Profile is enabled (Automated): PASS</li>
<li>Ensure that, if applicable, SELinux security options are set (Automated): WARN</li>
<p>Containers with no SecurityOptions:  reverent_noyce nice_blackburn</p>
<li>Ensure that Linux kernel capabilities are restricted within containers (Automated): PASS</li>
<li>Ensure that privileged containers are not used (Automated): PASS</li>
<li>Ensure sensitive host system directories are not mounted on containers (Automated): PASS</li>
<li>Ensure sshd is not run within containers (Automated): PASS</li>
<li>Ensure privileged ports are not mapped within containers (Automated): PASS</li>
<li>Ensure that only needed ports are open on the container (Manual): PASS</li>
<li>Ensure that the host's network namespace is not shared (Automated): PASS</li>
<li>Ensure that the memory usage for containers is limited (Automated): WARN</li>
<p>Container running without memory restrictions:  reverent_noyce nice_blackburn</p>
<li>Ensure that CPU priority is set appropriately on containers (Automated): WARN</li>
<p>Containers running without CPU restrictions:  reverent_noyce nice_blackburn</p>
<li>Ensure that the container's root filesystem is mounted as read only (Automated): WARN</li>
<p>Containers running with root FS mounted R/W:  reverent_noyce nice_blackburn</p>
<li>Ensure that incoming container traffic is bound to a specific host interface (Automated): PASS</li>
<li>Ensure that the 'on-failure' container restart policy is set to '5' (Automated): PASS</li>
<li>Ensure that the host's process namespace is not shared (Automated): PASS</li>
<li>Ensure that the host's IPC namespace is not shared (Automated): PASS</li>
<li>Ensure that host devices are not directly exposed to containers (Manual): PASS</li>
<li>Ensure that the default ulimit is overwritten at runtime if needed (Manual): INFO</li>
<p>Containers with no default ulimit override:  reverent_noyce nice_blackburn</p>
<li>Ensure mount propagation mode is not set to shared (Automated): PASS</li>
<li>Ensure that the host's UTS namespace is not shared (Automated): PASS</li>
<li>Ensure the default seccomp profile is not Disabled (Automated): PASS</li>
<li>Ensure that docker exec commands are not used with the privileged option (Automated): NOTE</li>
<li>Ensure that docker exec commands are not used with the user=root option (Manual): NOTE</li>
<li>Ensure that cgroup usage is confirmed (Automated): PASS</li>
<li>Ensure that the container is restricted from acquiring additional privileges (Automated): WARN</li>
<p>Containers without restricted privileges:  reverent_noyce nice_blackburn</p>
<li>Ensure that container health is checked at runtime (Automated): WARN</li>
<p>Containers without health check:  reverent_noyce nice_blackburn</p>
<li>Ensure that Docker commands always make use of the latest version of their image (Manual): INFO</li>
<li>Ensure that the PIDs cgroup limit is used (Automated): WARN</li>
<p>Containers without PIDs cgroup limit:  reverent_noyce nice_blackburn</p>
<li>Ensure that Docker's default bridge 'docker0' is not used (Manual): INFO</li>
<p>Containers using docker0 network:  3031a689826da0bfe570e50d0752ae08f4230ed94cf14099a4fc46c4e7a10755:reverent_noyce e71ad4feabcef64c1de640af5011b7686502e1dfac69fefa0e7b6f50d2d59cf0:nice_blackburn</p>
<li>Ensure that the host's user namespaces are not shared (Automated): PASS</li>
<li>Ensure that the Docker socket is not mounted inside any containers (Automated): PASS</li>
</ul>
<h3>Docker Security Operations</h3>
<ul>
<li>Ensure that image sprawl is avoided (Manual): INFO</li>
<p>7 active/8 in use</p>
<li>Ensure that container sprawl is avoided (Manual): INFO</li>
<p>7 total/2 running</p>
</ul>
<h3>Docker Swarm Configuration</h3>
<ul>
<li>Ensure that the minimum number of manager nodes have been created in a swarm (Automated): PASS</li>
<li>Ensure that swarm services are bound to a specific host interface (Automated): PASS</li>
<li>Ensure that all Docker swarm overlay networks are encrypted (Automated): PASS</li>
<li>Ensure that Docker's secret management commands are used for managing secrets in a swarm cluster (Manual): PASS</li>
<li>Ensure that swarm manager is run in auto-lock mode (Automated): PASS</li>
<li>Ensure that the swarm manager auto-lock key is rotated periodically (Manual): PASS</li>
<li>Ensure that node certificates are rotated as appropriate (Manual): PASS</li>
<li>Ensure that CA certificates are rotated as appropriate (Manual): PASS</li>
<li>Ensure that management plane traffic is separated from data plane traffic (Manual): PASS</li>
</ul>
</body>
</html>
```
