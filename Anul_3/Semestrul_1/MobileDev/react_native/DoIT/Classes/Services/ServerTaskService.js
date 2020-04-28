'use strict';

import {Task} from '../Model/Task.js'
import {ProjectService} from './ProjectService.js'
import {Project} from '../Model/Project.js'

export class ServerTaskService {

    static instance;

    formatDate(date) {
        console.log(date);
        if (date == null) {
            return null;
        }
        var day = date.getDate();
        var monthIndex = date.getMonth();
        var year = date.getFullYear();

        return year + '-' + monthIndex + '-' + day;
    }

    constructor() {
        if(ServerTaskService.instance) {
            return ServerTaskService.instance
        }

        ServerTaskService.instance = this
    }

    parseDate(input) {
        var parts = input.split('-');
        return new Date(parts[0], parts[1], parts[2]); // Note: months are 0-based
    }

    getTasks(completed, callback) {
        fetch('http://localhost:8080/task/get', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then((response) => response.json())
        .then((responseJson) => {
            var tasks = responseJson["object"]["tasks"];

            console.log(tasks);

            var responseTasks = [];

            for (var index in tasks) {
                var project = new Project(tasks[index]["project"]["name"], tasks[index]["project"]["id"]);
                var task = new Task(tasks[index]["name"], tasks[index]["description"], this.parseDate(tasks[index]["dueDate"]), project, tasks[index]["id"]);
                task.isCompleted = tasks[index]["isCompleted"];
                task.completedDate = tasks[index]["completedDate"];
                responseTasks.push(task);
            }

            console.log(responseTasks);
            console.log(completed);

            var tasksToReturn = responseTasks.filter((item) => {
                return item.isCompleted == completed;
            })

            console.log(tasksToReturn);

            callback(tasksToReturn);
        })
        .catch((error) => {
            console.error(error);
            callback(null);
        });
    }

    completeTask(task, callback) {
        task.isCompleted = true;
        task.completedDate = new Date();
        this.update(task.id, task, callback);
    }

    saveTask(task, callback) {
        fetch('http://localhost:8080/task/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: task.name,
                description: task.description,
                dueDate: this.formatDate(task.dueDate),
                projectId: task.project.id
            })
        })
        .then((response) => response.json())
        .then((responseJson) => {
            var newId = responseJson["object"];

            callback(newId);
        })
        .catch((error) => {
            console.error(error);
            callback(null);
        });
    }

    deleteTask(task, callback) {
        fetch('http://localhost:8080/task/delete/' + task.id, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then((response) => response.json())
        .then((responseJson) => {
            var success = responseJson["object"];

            callback(success);
        })
        .catch((error) => {
            console.error(error);
            callback(null);
        });
    }

    update(key, newTask, callback) {
        console.log(newTask.dueDate);
        console.log(newTask.completedDate);
        fetch('http://localhost:8080/task/update', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                id: key,
                name: newTask.name,
                description: newTask.description,
                dueDate: this.formatDate(newTask.dueDate),
                project: {
                    id: newTask.project.id,
                    name: newTask.project.name,
                },
                isCompleted: newTask.isCompleted,
                completionDate: this.formatDate(newTask.completedDate)
            })
        })
        .then((response) => response.json())
        .then((responseJson) => {
            var success = responseJson["object"];

            callback(success);
        })
        .catch((error) => {
            console.error(error);
            callback(null);
        });
    }
}
