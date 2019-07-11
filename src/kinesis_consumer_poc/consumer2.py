#!env python
from amazon_kclpy import kcl


class RecordProcessor(kcl.RecordProcessorBase):

    def initialize(self, initialiation_input):
        print("initialize")
        pass

    def process_records(self, process_records_input):
        print("process_records")
        pass

    def lease_lost(self, lease_lost_input):
        print("lease_lost")
        pass

    def shard_ended(self, shard_ended_input):
        print("shard_ended")
        pass

    def shutdown_requested(self, shutdown_requested_input):
        print("shutdown_requested")
        pass


if __name__ == "__main__":
    kclprocess = kcl.KCLProcess(RecordProcessor())
    kclprocess.run()
