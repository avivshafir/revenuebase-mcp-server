# RevenueBase MCP Server

A Model Context Protocol (MCP) server that provides access to RevenueBase's industry-leading email verification API. This server enables AI assistants and applications to verify business emails, including catch-all and firewall-protected domains, with over 99% accuracy.

## Features

- **Real-time Email Verification**: Verify individual email addresses instantly
- **Batch Email Processing**: Submit and process large email lists
- **Process Management**: Monitor, cancel, and track batch processing jobs
- **Credit Management**: Check remaining API credits
- **API Key Management**: Generate new API keys
- **High Accuracy**: Over 99% accuracy for B2B email verification
- **Catch-All Domain Support**: Verify catch-all email domains that other tools can't handle
- **Firewall Navigation**: Bypass email firewalls like Mimecast and Barracuda

## About RevenueBase

RevenueBase provides industry-leading email verification services specifically built for B2B data providers. With the ability to verify catch-all and firewall-protected domains, RevenueBase ensures maximum accuracy where other services fall short.

Learn more about RevenueBase's email verification services at: [https://revenuebase.ai/email-list-cleaning/](https://revenuebase.ai/email-list-cleaning/)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd revenuebase-mcp-server
```

2. Install dependencies using uv:
```bash
uv sync
```

3. Set up your RevenueBase API key:
```bash
export REVENUEBASE_API_KEY="your_api_key_here"
```

## Usage

### Running the Server

```bash
python server.py
```

The server will start and be available for MCP connections.

### Using with MCP Clients

#### Claude Desktop

To use this server with Claude Desktop, add the following configuration to your Claude Desktop config file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "revenuebase": {
      "command": "uv",
      "args": ["--directory", "/path/to/revenuebase-mcp-server", "run", "python", "server.py"],
      "env": {
        "REVENUEBASE_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

Replace `/path/to/revenuebase-mcp-server` with the actual path to your cloned repository and `your_api_key_here` with your actual RevenueBase API key.

#### Other MCP Clients

For other MCP clients, you can connect to the server using the stdio transport. The server runs as a standard MCP server and accepts connections on stdin/stdout.

Example using the MCP Python SDK:
```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="python",
    args=["server.py"],
    env={"REVENUEBASE_API_KEY": "your_api_key_here"}
)

async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        # Initialize the connection
        await session.initialize()
        
        # List available tools
        tools = await session.list_tools()
        print("Available tools:", [tool.name for tool in tools.tools])
        
        # Call a tool
        result = await session.call_tool("real_time_email_verification", {
            "email": "test@example.com"
        })
        print("Verification result:", result)
```

### Available Tools

#### 1. Real-time Email Verification
Verify a single email address instantly.

**Parameters:**
- `email` (string): The email address to verify

**Example:**
```python
real_time_email_verification("user@example.com")
```

#### 2. Batch Email Submission
Submit a file reference for batch email processing.

**Parameters:**
- `filename` (string): The filename reference for batch processing

**Example:**
```python
batch_email_submission("email_list.csv")
```

#### 3. Batch Process Status
Check the status of a batch email processing job.

**Parameters:**
- `process_id` (int): The ID of the batch processing job

**Example:**
```python
batch_process_email_status(12345)
```

#### 4. Queued Processes
List all queued email batch processing jobs.

**Example:**
```python
queued_process()
```

#### 5. Cancel Process
Cancel an ongoing or queued batch email processing job.

**Parameters:**
- `process_id` (int): The ID of the process to cancel

**Example:**
```python
cancel_process(12345)
```

#### 6. Get Credits
Retrieve the number of remaining credits for your account.

**Example:**
```python
get_credits()
```

#### 7. Generate New API Key
Generate and return a new API key.

**Example:**
```python
new_api_key()
```

## Configuration

### Environment Variables

- `REVENUEBASE_API_KEY`: Your RevenueBase API key (required)

### API Endpoints

The server connects to the following RevenueBase API endpoints:

- `https://api.revenuebase.ai/v1/process-email` - Real-time email verification
- `https://api.revenuebase.ai/v1/batch-process-email` - Batch email submission
- `https://api.revenuebase.ai/v1/batch-process-email-status` - Batch status check
- `https://api.revenuebase.ai/v1/queued-process` - List queued processes
- `https://api.revenuebase.ai/v1/cancel-process` - Cancel process
- `https://api.revenuebase.ai/v1/credits` - Get credits
- `https://api.revenuebase.ai/v1/new-api-key` - Generate new API key

## Error Handling

All tools include proper error handling and will raise `RuntimeError` if the API key is not configured. HTTP errors from the RevenueBase API are automatically raised using `requests.raise_for_status()`.

## Requirements

- Python 3.7+
- fastmcp
- requests

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For RevenueBase API support and documentation, visit:
- [RevenueBase Email Verification](https://revenuebase.ai/email-list-cleaning/)
- [RevenueBase API Documentation](https://revenuebase.ai/api-documentation)

For issues with this MCP server, please open an issue in this repository.
