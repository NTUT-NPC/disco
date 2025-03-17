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

Get your Discord token by following [this guide](https://gist.github.com/MarvNC/e601f3603df22f36ebd3102c501116c6)

### Running with Docker

```sh
docker run -d \
  --name disco \
  --restart unless-stopped \
  -e DISCORD_TOKEN=YOUR_DISCORD_TOKEN \
  ghcr.io/ntut-npc/disco:latest
```

### Running locally

1. Copy `.env.example` to `.env` and fill in your Discord token:

    ```sh
    cp .env.example .env
    # Edit .env with your favorite editor
    ```

2. Run the bot with `uv`:

    ```sh
    uv run bot.py
    ```

3. Keep the bot online and party all night long! 🎉
