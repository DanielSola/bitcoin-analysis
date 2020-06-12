## Bitcoin Blockchain Analysis

<img src="https://mk0blockchaineswlkle.kinstacdn.com/wp-content/uploads/2017/06/Cadena-de-bloques-1024x314.png" alt="MarineGEO circle logo" />



Basic analysis of Bitcoin blockchain data. Bitcoin is a decentralized cryptocurrency that operates sending transactions through a P2P network. These transacctions are grouped in an structure known as block.

Analysis performed
- Number of transactions per block
- Transaction value of each block
- Time between blocks
- Average block size per hour
- Number of transactions per hour

Data has been obtained from Coinbase and corresponds to market data from days 31/05/2020 and 01/06/2020

### Run instructions

1. Clone repone to your machine 

2. Download files `blocks.json` and `txs.json` from *[here](https://drive.google.com/file/d/1xLO-BISgwKRqNpDefF8I240HNh7xfU5A/view)*  (1.2GB)

3. Place downloaded files in folder `/data`

4. Run file `basic_analysis.py` with Python 3
5. Plot results are generated in folder `/images`

### Run test

Run unit test by executing file `test.py` in Python3