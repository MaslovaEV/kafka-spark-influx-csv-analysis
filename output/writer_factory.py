import errors
from .csv_writer import CSVWriter
from .std_out_writer import StdOutWriter

class WriterFactory:
    def instance_writer(self, output_config):
        output = output_config.content["output"]
        if output["method"] == "csv":
            return CSVWriter(output["options"]["csv"]["path"], output["options"]["csv"]["sep"],
                      output["options"]["csv"]["encoding"])
        elif output["method"] == "stdout":
            return StdOutWriter()

        raise errors.UnsupportedOutputFormat("Format {} not supported".format(output["method"]))
