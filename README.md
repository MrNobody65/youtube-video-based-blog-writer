# youtube-video-based-blog-writer

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
This is a mini project to learn CrewAI framework. This project allows user to write a blog of a `<topic>` base on the content of videos from a specific Youtube channel.

### Built With
* [![CrewAI][CrewAI-logo]][CrewAI-url]

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
* Have a active API key from [OpenAI](https://platform.openai.com/settings/organization/api-keys).

### Installation
1. Clone the repository from Github:
    ```sh
    git clone https://github.com/MrNobody65/youtube-video-based-blog-writer.git
    ```
2. Create and activate python virtual environment with `conda`
    ```sh
    conda create -p venv python==3.10.0
    conda activate ./venv
    ```
3. Install dependencies
    ```sh
    pip install -r requirements.txt
    ```

4. Create `.env` file based on `.env.example` and enter your OpenAI API key.

5. Run the application
    ```sh
    python crew.py <topic>
    ```

<!-- ACKNOWLEDGEMENT -->
## Acknowledgement
* [crewAI Crash Course For Beginners-How To Create Multi AI Agent For Complex Usecases](https://www.youtube.com/watch?v=UV81LAb3x2g)

<!-- MARKDOWN LINKS & IMAGES -->
[CrewAI-logo]: https://img.shields.io/badge/CrewAI-D00020?style=for-the-badge&labelColor=000000
[CrewAI-url]: https://www.crewai.com