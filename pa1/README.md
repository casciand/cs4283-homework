# Assignment 1

## Run

YAML files are defined under the `v1` namespace.

1. Install and configure Docker and Kubernetes.
2. Create clusters using `start_k8s.sh`.
3. Apply YAML files for each cluster in `/flatbuffers/kubernetes` and `protobuffers/kubernetes` respectfully.
4. Check container logs to see serialized/deserialized messages with `kubectl logs POD_NAME -n v1`.

## Demo

https://drive.google.com/file/d/1-4ggb23ZkSsbkNfrH5CMVyAZvlNrSXE3/view?usp=sharing

## Results
<p>
<img src="https://github.com/VUComputerNetworks/og_team15/blob/main/pa1/Latencies.png" alt="Latencies">
</p>

## Teamwork

Andrew: Added serialization and deserialization for all message types with flatbuffers. Added serialization for order 
message with protocol buffers. Created and hosted Docker images for both clusters.

Kev: Added serialization for health and response messages with protocol buffers. Added socket capabilities with ZeroMQ
and gRPC.

Binh: Worked on serializing and deserializing order message with flatbuffers. Orchestrated Kubernetes clusters and 
wrote YAML files.

Work was distributed evenly.
