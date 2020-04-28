'use strict';

import {Task} from '../Model/Task.js'
import {ProjectService} from './ProjectService.js'
import {Project} from '../Model/Project.js'
import {AsyncStorage} from 'react-native'

export class TaskService {

    static instance;

    constructor() {
        if(TaskService.instance) {
            return TaskService.instance
        }

        TaskService.instance = this
    }

    getTasks(completed, callback) {
        AsyncStorage.getItem('@MyTasks:key').then((value) => {
            console.log(value);
            var tasks = JSON.parse(value);

            var tasksToReturn = tasks.filter((item) => {
                return item.isCompleted == completed;
            })

            callback(tasksToReturn);
        }).catch((err) => {
            callback(null);
        })
    }

    completeTask(task, callback) {
        AsyncStorage.getItem('@MyTasks:key').then((value) => {
            var tasks = JSON.parse(value);

            var idLists = tasks.map(function(e) { return e.id; })
            var index = idLists.indexOf(task.id);

            if (index > -1) {

                tasks[index].isCompleted = true
                tasks[index].completedDate = new Date();

                AsyncStorage.setItem('@MyTasks:key', JSON.stringify(tasks)).then(() => {
                    callback(true);
                }).catch((err) => {
                    callback(false);
                })
            } else {
                callback(false);
            }
        }).catch((err) => {
            callback(false);
        })
    }

    saveTask(task, callback) {
        AsyncStorage.getItem('@MyTasks:key').then((value) => {
            var tasks = JSON.parse(value);
            var idLists = tasks.map(function(e) { return e.id; });
            var index = idLists.indexOf(task.id);
            if (index > -1) {
                callback(false);
            } else {
                tasks.push(task);
                AsyncStorage.setItem('@MyTasks:key', JSON.stringify(tasks)).then(() => {
                    callback(tasks)
                }).catch((err) => {
                    callback(false)
                })
            }
        }).catch((err) => {
            callback(false);
        })
    }

    deleteTask(task, callback) {
        AsyncStorage.getItem('@MyTasks:key').then((value) => {
            var tasks = JSON.parse(value);
            var idLists = tasks.map(function(e) { return e.id; });
            var index = idLists.indexOf(task.id);
            if (index > -1) {
                tasks.splice(index, 1);
                AsyncStorage.setItem('@MyTasks:key', JSON.stringify(tasks)).then(() => {
                    callback(true);
                }).catch((err) => {
                    callback(false);
                })
            } else {
                callback(false);
            }
        }).catch((err) => {
            callback(false);
        })
    }

    update(key, newTask, callback) {
        AsyncStorage.getItem('@MyTasks:key').then((value) => {
            var tasks = JSON.parse(value);
            var idLists = tasks.map(function(e) { return e.id; });
            var index = idLists.indexOf(key);
            if (index > -1) {
                tasks[index].name = newTask.name;
                tasks[index].dueDate = newTask.dueDate;
                tasks[index].project = newTask.project;
                tasks[index].description = newTask.description;
                AsyncStorage.setItem('@MyTasks:key', JSON.stringify(tasks)).then(() => {
                    callback(true);
                }).catch((err) => {
                    callback(false);
                })
            } else {
                callback(false);
            }
        }).catch((err) => {
            callback(false);
        })
    }
}
