from langserve import RemoteRunnable

# Initialize the remote chain with the server's URL
remote_chain = RemoteRunnable("http://localhost:8000/chain/")

# Make a translation request
response = remote_chain.invoke({
    "language": "italian",
    "text": "hi"
})
print(response)  # Expected output: "ciao"