#work with log

import logger

print ("Hello world")

log = logger.get_logger(__name__)
log.debug("Debug-level message")
log.info("Info-level message")
log.warning("Warning-level message")
log.error("Error-level message")
