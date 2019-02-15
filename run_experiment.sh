echo 'start run_experiment' >> /local/repository/run_experiment_note1.txt

bash kubernetes_setup.sh

echo 'start run_experiment n2' >> /local/repository/run_experiment_note2.txt

bash deploy_application.sh $1

echo 'start run_experiment n3' >> /local/repository/run_experiment_note3.txt

: ' TODO
EXP_NAME = None # TODO
CONFIG_FILE = None # TODO
PORT_NUMBER = None # TODO
VM_IP = Nonee # TODO
/mydata/mimir_snakemake_t2/experiment_coordinator/run_experiment.py --exp_name EXP_NAME --config_file CONFIG_FILE --prepare_app_p --port PORT_NUMBER -ip VM_IP --no_exfil
'
echo 'start run_experiment n4' >> /local/repository/run_experiment_note4.txt
