<?php

use Illuminate\Support\Facades\Gate;
use Illuminate\Support\Facades\DB;

use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;

$app->group(['middleware' => 'auth'], function () use ($app) {

    $app->get('/test-python', function () {
        if (Gate::denies('onboarding')) {
            return response('Forbidden', 403);
        }

        $process = new Process(env('PYTHON_ENV') . " " . env('PYTHON_DIR') . "main.py python_test");
        $process->run();
        if (!$process->isSuccessful()) {
            throw new ProcessFailedException($process);
        }
        echo $process->getOutput();
    });

    $app->get('/create-agol-group/{groupId}', function ($groupId) {
        if (Gate::denies('onboarding')) {
            return response('Forbidden', 403);
        }
        $usernames = app()->request->input('usernames');

        $process = new Process(env('PYTHON_ENV') . " " . env('PYTHON_DIR') . "main.py create_group \"{$groupId}\" \"{$usernames}\"");
        $process->run();
        if (!$process->isSuccessful()) {
            throw new ProcessFailedException($process);
        }
        echo $process->getOutput();
    });

    $app->get('/download-collector-one-group/{groupId}', function ($groupId) {
        if (Gate::denies('sync-data')) {
            return response('Forbidden', 403);
        }

        $process = new Process(env('PYTHON_ENV') . " " . env('PYTHON_DIR') . "main.py download_collector_one_group \"{$groupId}\"");
        $process->run();
        if (!$process->isSuccessful()) {
            throw new ProcessFailedException($process);
        }
        echo $process->getOutput();
    });

    $app->get('/download-all-agol-one-group/{groupId}', function ($groupId) {
        if (Gate::denies('sync-data')) {
            return response('Forbidden', 403);
        }

        $process1 = new Process(env('PYTHON_ENV') . " " . env('PYTHON_DIR') . "main.py download_collector_one_group \"{$groupId}\"");
        $process1->run();
        if (!$process1->isSuccessful()) {
            throw new ProcessFailedException($process1);
        }

        $process2 = new Process(env('PYTHON_ENV') . " " . env('PYTHON_DIR') . "main.py download_survey123");
        $process2->run();
        if (!$process2->isSuccessful()) {
            throw new ProcessFailedException($process2);
        }
        echo $process1->getOutput() . $process2->getOutput();
    });

    $app->get('/download-all-agol', function () {
        if (Gate::denies('onboarding')) {
            return response('Forbidden', 403);
        }

        echo "Success:  You have successfully started the process for downloading all AGOL data.  This function takes a long time to load, so we won't keep you waiting.  It is best to check the database in a couple of minutes to see the results.||";
        $process = new Process(env('PYTHON_ENV') . " " . env('PYTHON_DIR') . "main.py download_all_agol_data");
        $process->run();
        if (!$process->isSuccessful()) {
            throw new ProcessFailedException($process);
        }
        echo $process->getOutput();
    });

    $app->get('/download-survey123', function () {
        if (Gate::denies('onboarding')) {
            return response('Forbidden', 403);
        }

        $process = new Process(env('PYTHON_ENV') . " " . env('PYTHON_DIR') . "main.py download_survey123");
        $process->run();
        if (!$process->isSuccessful()) {
            throw new ProcessFailedException($process);
        }
        echo $process->getOutput();
    });
});
