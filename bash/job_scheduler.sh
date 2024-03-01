#!/bin/bash

folder_path="src/config/research/job_scheduler/batches"
folder_ongoing="src/config/research/job_scheduler/batches_ongoing"
folder_processed="src/config/research/job_scheduler/batches_processed"
folder_fault="src/config/research/job_scheduler/batches_fault"

while true; do
    files=($folder_path/*)
    if [ ${#files[@]} -eq 0 ] || [ ${#files[@]} -eq 1 -a "${files[0]}" = "$folder_path/*" ]; then
        echo "No files found. Exiting."
        break
    fi
    selected_file=${files[$RANDOM % ${#files[@]}]}

    echo "#############################################"

    echo "Abs path selected file: $selected_file"

    selected_file_no_extension=$(basename "$selected_file" | sed 's/\.yaml$//')
    echo "Selected file no extension: $selected_file_no_extension"

    mv "$selected_file" "$folder_ongoing"
    echo "File moved to ongoing folder."

    echo "#############################################"

    python3 src/main.py --research_config="$selected_file_no_extension" --batch_job=True --use_cuda=True

    python_exit_status=$?

    echo "#############################################"

    echo "Python exit status: $python_exit_status"
    
    if [ $python_exit_status -eq 0 ]; then
        echo "Python execution successful. Moving file."
        # Move file if Python execution was successful
        mv "$folder_ongoing/$selected_file_no_extension.yaml" "$folder_processed"

    else
        echo "Python execution failed. Trying with use_cuda=False."
        python3 src/main.py --research_config="$selected_file_no_extension" --batch_job=True --use_cuda=False

        python_exit_status=$?

        echo "#############################################"

        echo "Python exit status: $python_exit_status"

        if [ $python_exit_status -eq 0 ]; then
            echo "Python execution successful with use_cuda=False. Moving file."
            # Move file if Python execution was successful with use_cuda=False
            mv "$folder_ongoing/$selected_file_no_extension.yaml" "$folder_processed"
        else
            echo "Python execution failed with use_cuda=False. Moving file to error folder."
            mv "$folder_ongoing/$selected_file_no_extension.yaml" "$folder_fault"
        fi
    fi



    echo "#############################################"
done
