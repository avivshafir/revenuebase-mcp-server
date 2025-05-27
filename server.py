from fastmcp import FastMCP
import requests
import os

mcp = FastMCP("Revenuebase mcp server")

api_key = os.getenv("REVENUEBASE_API_KEY")


@mcp.tool()
def batch_process_email_status(process_id: int) -> dict:
    """
    Retrieves status of batch email processing job.
    """
    if not api_key:
        raise RuntimeError("Environment variable REVENUEBASE_API_KEY is not set")
    url = "https://api.revenuebase.ai/v1/batch-process-email-status"
    headers = {
        "x-key": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {"process_id": process_id}
    resp = requests.post(url, json=payload, headers=headers, verify=False)
    resp.raise_for_status()
    return resp.json()


@mcp.tool()
def queued_process() -> dict:
    """
    Lists all queued email batch processing jobs.
    """
    if not api_key:
        raise RuntimeError("Environment variable REVENUEBASE_API_KEY is not set")
    url = "https://api.revenuebase.ai/v1/queued-process"
    headers = {"x-key": api_key, "Accept": "application/json"}
    resp = requests.get(url, headers=headers, verify=False)
    resp.raise_for_status()
    return resp.json()


@mcp.tool()
def get_credits() -> dict:
    """
    Retrieves the number of remaining credits for the authenticated user.
    """
    if not api_key:
        raise RuntimeError("Environment variable REVENUEBASE_API_KEY is not set")
    url = "https://api.revenuebase.ai/v1/credits"
    headers = {"x-key": api_key, "Accept": "application/json"}
    resp = requests.get(url, headers=headers, verify=False)
    resp.raise_for_status()
    return resp.json()


@mcp.tool()
def new_api_key() -> dict:
    """
    Generates and returns a new API key for the user.
    """
    if not api_key:
        raise RuntimeError("Environment variable REVENUEBASE_API_KEY is not set")
    url = "https://api.revenuebase.ai/v1/new-api-key"
    headers = {"x-key": api_key, "Accept": "application/json"}
    resp = requests.get(url, headers=headers, verify=False)
    resp.raise_for_status()
    return resp.json()


@mcp.tool()
def real_time_email_verification(email: str) -> dict:
    """
    Verifies a single email address using the Revenuebase API.
    """
    if not api_key:
        raise RuntimeError("Environment variable REVENUEBASE_API_KEY is not set")
    url = "https://api.revenuebase.ai/v1/process-email"
    headers = {
        "x-key": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {"email": email}
    resp = requests.post(url, json=payload, headers=headers, verify=False)
    resp.raise_for_status()
    return resp.json()


@mcp.tool()
def batch_email_submission(filename: str) -> dict:
    """
    Submits a file reference for batch email processing using the Revenuebase API.
    """
    if not api_key:
        raise RuntimeError("Environment variable REVENUEBASE_API_KEY is not set")
    url = "https://api.revenuebase.ai/v1/batch-process-email"
    headers = {
        "x-key": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {"filename": filename}
    resp = requests.post(url, json=payload, headers=headers, verify=False)
    resp.raise_for_status()
    return resp.json()


@mcp.tool()
def cancel_process(process_id: int) -> dict:
    """
    Cancels an ongoing or queued batch email processing job using the Revenuebase API.
    """
    if not api_key:
        raise RuntimeError("Environment variable REVENUEBASE_API_KEY is not set")
    url = "https://api.revenuebase.ai/v1/cancel-process"
    headers = {
        "x-key": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {"process_id": process_id}
    resp = requests.post(url, json=payload, headers=headers, verify=False)
    resp.raise_for_status()
    return resp.json()


if __name__ == "__main__":
    mcp.run()
