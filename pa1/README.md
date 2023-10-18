# Assignment 1

## Run

YAML files are defined under the `v1` namespace.

1. Install and configure Docker and Kubernetes.
2. Create clusters using `start_k8s.sh`.
3. Apply YAML files for each cluster in `/flatbuffers/kubernetes` and `protobuffers/kubernetes` respectfully.
4. Check container logs to see serialized/deserialized messages with `kubectl logs POD_NAME -n v1`.

## Results

## Teamwork

Andrew: Added serialization and deserialization for all message types with flatbuffers. Added serialization for order 
message with protocol buffers. Created and hosted Docker images for both clusters.