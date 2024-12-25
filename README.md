<p align="center">
  <img src="docs/TwemojiPartyPopper.svg" alt="Disco Logo" align="center" width="128" height="128">
</p>

<h1 align="center">Disco</h1>

<p align="center">
  A Discord bot keeping your account online. Party all night long! 🎉
</p>

<p align="center">
  <a href="https://ntut.club">
    <img
      alt="An NPC Project"
      src="https://img.shields.io/badge/An_NPC_Project-333?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzMiAzMiIgZmlsbD0iI2ZmZiI%2BPHBhdGggZD0iTTQgNHYyNGw4LTggMTYgOFY0bC04IDh6Ii8%2BPC9zdmc%2B"
    >
  </a>
</p>

## Usage

1. Get your Discord token by following [this guide](https://gist.github.com/MarvNC/e601f3603df22f36ebd3102c501116c6)

2. Write a Docker Compose file like this:

    ```yaml
    services:
      disco:
        image: ghcr.io/NTUT-NPC/disco:latest
        container_name: disco
        environment:
          - DISCORD_TOKEN=YOUR_DISCORD_TOKEN
        restart: unless-stopped
    ```

3. Run `docker-compose up -d` to start the bot

4. Keep the bot online and party all night long! 🎉
