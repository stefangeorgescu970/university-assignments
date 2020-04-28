'use strict';

import {Project} from '../Model/Project.js'
import {AsyncStorage} from 'react-native'

export class ProjectService {

    static instance;

    constructor() {
        if(ProjectService.instance) {
            return ProjectService.instance
        }

        ProjectService.instance = this
    }

    getProjects(callback) {
        AsyncStorage.getItem('@MyProjects:key').then((value) => {
            console.log("Get all projects: " + value);
            var projects = JSON.parse(value);
            callback(projects);
        }).catch((err) => {
            // callback(null);
        })
    }

    getProject(byId, callback) {
        AsyncStorage.getItem('@MyProjects:key').then((value) => {
            var projects = JSON.parse(value);
            var idLists = projects.map(function(e) { return e.id; });
            var index = idLists.indexOf(byId);
            if (index > -1) {
                callback(projects[index]);
            } else {
                callback(null);
            }
        }).catch((err) => {
            callback(null);
        })
    }

    saveProject(project, callback) {
        AsyncStorage.getItem('@MyProjects:key').then((value) => {
            var projects = JSON.parse(value);
            var idLists = projects.map(function(e) { return e.id; });
            var index = idLists.indexOf(project.id);
            if (index > -1) {
                callback(false);
            } else {
                projects.push(project);
                AsyncStorage.setItem('@MyProjects:key', JSON.stringify(projects)).then(() => {
                    callback(projects);
                }).catch((err) => {
                    callback(false)
                })
            }
        }).catch((err) => {
            callback(false);
        })
    }

    deleteProject(project, callback) {
        AsyncStorage.getItem('@MyProjects:key').then((value) => {
            var projects = JSON.parse(value);
            var idLists = projects.map(function(e) { return e.id; });
            var index = idLists.indexOf(project.id);
            if (index > -1) {
                projects.splice(index, 1);
                AsyncStorage.setItem('@MyProjects:key', JSON.stringify(projects)).then(() => {
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
