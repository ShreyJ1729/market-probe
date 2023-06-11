import os
import modal

image = modal.Image.debian_slim()

stub = modal.Stub("market-probe", image=image)


@stub.function(gpu=modal.gpu.A100(memory=20))
@modal.web_endpoint(method="GET")
def get_eod_data():
    pass


def main():
    pass

if __name__ == "__main__":
    main()