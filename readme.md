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

