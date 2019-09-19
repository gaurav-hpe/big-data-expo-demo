!/bin/sh
set -o pipefail
SELF=$(readlink -nf $0)
export CONFIG_BASE_DIR=$(dirname ${SELF})
source ${CONFIG_BASE_DIR}/logging.sh
source ${CONFIG_BASE_DIR}/utils.sh
source ${CONFIG_BASE_DIR}/macros.sh
FQDN="$(invoke_bdvcli --get node.fqdn)"
ROLE="$(invoke_bdvcli --get node.role_id)"
#

REGISTER_START_SERVICE_SYSCTL dss dss.service
