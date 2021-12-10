import json
import logging
import grpc
import protogen.coresrv_pb2 as coresrv_pb2
import protogen.coresrv_pb2_grpc as coresrv_pb2_grpc
import os


coresrv_address = os.environ['CORE_SERVICE_ADDRESS'] or 'coresrv:50050'


def main():
    with grpc.insecure_channel(coresrv_address) as channel:
        with open("./dataset.json", "r+") as datafile:
            jsondata = json.load(datafile)
            req = coresrv_pb2.BulkStoreGameSalesRequest(items=jsondata)
            stub = coresrv_pb2_grpc.CoreServiceStub(channel)
            res = stub.BulkStoreGameSales(req)
            print(len(res.items))


if __name__ == "__main__":
    logging.basicConfig()
    main()
