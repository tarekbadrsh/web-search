# Search Engine with AI Summarization

A powerful and flexible search engine application that enables users to search the web, retrieve comprehensive results with full content extraction, and generate AI-powered summaries. The application supports both a Command Line Interface (CLI) and a REST API, making it suitable for terminal users and application integration alike.

## Features

- **Multiple Search Types**: Supports searches for text, news, images, and videos.
- **Full Content Extraction**: Retrieves and parses the complete content of search results using the Jina Reader API.
- **AI-Powered Summarization**: Generates concise summaries of search results using Groq AI.
- **Dual Interfaces**:
  - Command Line Interface (CLI) for easy terminal-based access.
  - REST API for programmatic integration.
- **Flexible Search Options**: Allows customization of region, time limits, and maximum results.

## Installation

To set up the application, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/search-engine.git
   cd search-engine
   ```

   *Replace `yourusername` with your actual GitHub username or the correct repository URL.*

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   *Note*: The `requirements.txt` file includes most dependencies, but you may need to manually install the `groq` package if it’s not listed:

   ```bash
   pip install groq
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add your API keys:

   ```bash
   JINA_API_KEY=your_jina_api_key
   GROQ_API_KEY=your_groq_api_key
   ```

   Replace `your_jina_api_key` and `your_groq_api_key` with your actual API keys from Jina and Groq, respectively. These keys are required for content extraction and AI summarization.

## Usage

### Command Line Interface (CLI)

To perform a search via the CLI, use the following command:

```bash
python main.py cli search "your search query"
```

#### Options

Customize your search with these optional parameters:

- `--search-type`: Type of search (`text`, `news`, `images`, `videos`). Default: `text`.
- `--max-results`: Maximum number of results to return. Default: 5.
- `--timelimit`: Time limit for results (`d` for day, `w` for week, `m` for month). Default: None.
- `--region`: Region code for results (e.g., `us-en`, `uk-en`; applicable for `news`, `images`, `videos`). Default: None.

#### Example

```bash
python main.py cli search "python programming" --search-type text --max-results 10 --timelimit w --region us-en
```

Results, including full content and an AI-generated summary, are saved to a JSON file named with the current timestamp (e.g., `1634567890.json`).

### REST API

To start the API server, run:

```bash
python main.py api
```

The server will be available at `http://0.0.0.0:8000`.

#### Search Endpoint

- **Endpoint**: `GET /search?q=your+search+query`
- **Optional Query Parameters**:
  - `search_type`: Type of search (`text`, `news`, `images`, `videos`). Default: `text`.
  - `max_results`: Maximum number of results. Default: 5.
  - `timelimit`: Time limit for results (`d`, `w`, `m`). Default: None.
  - `region`: Region code for results. Default: None.

#### Example Requests

- Basic search:

  ```
  http://0.0.0.0:8000/search?q=hello
  ```

- Advanced search:

  ```
  http://0.0.0.0:8000/search?q=sudan-war&search_type=news&max_results=10&timelimit=d
  ```

The API returns a JSON response containing search results, full content, and an AI-generated summary.

## Configuration

The application requires API keys for external services:

- **Jina Reader API**: Used for content extraction. Set `JINA_API_KEY` in the `.env` file.
- **Groq AI**: Used for summarization. Set `GROQ_API_KEY` in the `.env` file.

Ensure the `.env` file is created as described in the **Installation** section and kept secure (e.g., add it to `.gitignore` to avoid committing it to version control).

## How It Works

1. **Search**: The application queries DuckDuckGo’s search API to retrieve results based on the user’s input and options.
2. **Content Extraction**: For each result, it fetches the full content using the Jina Reader API.
3. **AI Summarization**: The extracted content is summarized using Groq AI, with the summarization behavior defined in `summary_system_prompt.md`.
4. **Output**:
   - **CLI**: Results are saved to a JSON file.
   - **API**: Results are returned as a JSON response.

## Dependencies

The application depends on the following Python libraries:

- `click`: For the CLI interface.
- `duckduckgo-search`: For performing searches via DuckDuckGo.
- `fastapi`: For the REST API framework.
- `requests`: For HTTP requests to the Jina Reader API.
- `uvicorn`: For running the API server.
- `groq`: For AI summarization.

Install all dependencies with:

```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to the repository to improve the application.

## Notes

- **API Keys**: The application will not function without valid Jina and Groq API keys. Obtain these from their respective services.
- **Custom Summarization**: The AI summarization behavior can be customized by editing `summary_system_prompt.md`, though this is optional for basic use.
- **License**: Currently, no license is specified. Consider adding a `LICENSE` file (e.g., MIT License) to clarify usage terms.
