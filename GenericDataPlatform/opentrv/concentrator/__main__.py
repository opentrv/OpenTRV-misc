import sys
import logging
import opentrv.concentrator

# Main entry into the system. This code is called when the concentrator
# module is run from the command line using the python -m option.
if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.info("Starting concentrator")
    parser = opentrv.concentrator.OptionParser()
    options = parser.parse(sys.argv)
    core = opentrv.concentrator.Core(options)
    core.run()
