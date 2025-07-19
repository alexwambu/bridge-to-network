import streamlit as st
import requests
import json

st.set_page_config(page_title="GBT Unified Bridge", layout="wide")
st.title("🌐 GBT Layer1 ↔ Layer2 + Ethereum/BNB/Polygon Bridge")

# RPC endpoints
RPC_ENDPOINTS = {
    "GBT_L1": "http://localhost:8545",
    "GBT_L2": "http://GBTNetwork:8545",
    "Ethereum Mainnet": "https://mainnet.infura.io/v3/YOUR_INFURA_KEY",
    "BNB Chain": "https://bsc-dataseed.binance.org/",
    "Polygon": "https://polygon-rpc.com",
    "Avalanche": "https://api.avax.network/ext/bc/C/rpc",
    "Arbitrum": "https://arb1.arbitrum.io/rpc",
    "Optimism": "https://mainnet.optimism.io"
}

CHAIN_OPTIONS = list(RPC_ENDPOINTS.keys())
from_chain = st.selectbox("From Chain", CHAIN_OPTIONS)
to_chain = st.selectbox("To Chain", CHAIN_OPTIONS)

st.markdown("#### JSON-RPC Payload")
default_payload = '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
payload = st.text_area("Payload", value=default_payload, height=200)

if st.button("Relay / Send RPC"):
    try:
        headers = {"Content-Type": "application/json"}
        res = requests.post(RPC_ENDPOINTS[from_chain], data=payload, headers=headers, timeout=10)
        st.code(f"RPC Result from {from_chain}:", language="bash")
        st.json(res.json())

        # Simulate relaying: L1 auto-mints to L2
        if from_chain == "GBT_L1" and to_chain == "GBT_L2":
            st.success("✅ Auto-mint simulated on Layer 2 (via relayer logic)")
    except Exception as e:
        st.error(f"❌ RPC Error: {e}")
