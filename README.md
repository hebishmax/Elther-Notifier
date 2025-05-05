# Ether Notifier
Ether Notifier is an open-source application that helps Web3 developers know whether the social and technical network is "busy" or "available" for their projects by reading live data and alerting them intelligently.

## Features
- Connects to external sources such as the GitHub API to read activity.
- Binds the results to a smart contract written in Vyper on the Ethereum network.
- Simple CLI interface that allows direct verification or update.
- 100% free and open source.
- **FastAPI** backend for creating a fast and scalable web API interface to check the network status and interact with the service. This provides an **optional graphical interface** for developers who prefer HTTP-based interaction.

## Requirements
- Python 3.7 or higher
- `web3.py` library
- `requests` library
- FastAPI
- A running Ethereum node or an Infura account for Ethereum mainnet access.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/hebishmax/Elther-Notifier.git
    cd Elther-Notifier
    ```

2. Install the required Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Ethereum node connection or Infura credentials:
    - Obtain an **Infura** API key and replace `YOUR_INFURA_KEY` in the code with your key.

4. Set up the smart contract:
    - Ensure your contract address and ABI are correctly specified in the project.

## FastAPI Setup
Ether Notifier now includes a **FastAPI** backend that allows developers to interact with the service via HTTP requests. This provides a **scalable and easy way** to access network status and interact with smart contracts, but it remains **optional**. Developers who prefer working via the command line can continue using the **CLI** interface.

### Running FastAPI
You can start the FastAPI server using the following command:

```bash
uvicorn main:app --reload
