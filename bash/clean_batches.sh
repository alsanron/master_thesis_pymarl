#!/bin/bash
echo "Cleaning batches folder"

job_scheduler_path="src/config/research/job_scheduler"

rm -r $job_scheduler_path/batches/*
rm -r $job_scheduler_path/batches_fault/*
rm -r $job_scheduler_path/batches_ongoing/*
rm -r $job_scheduler_path/batches_processed/*