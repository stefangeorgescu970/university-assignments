'use strict';

import {Project} from '../Model/Project.js'

export class ServerProjectService {

    static instance;

    constructor() {
        if(ServerProjectService.instance) {
            return ServerProjectService.instance
        }

        ServerProjectService.instance = this
    }

    getProjects(callback) {
        fetch('http://localhost:8080/project/get', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then((response) => response.json())
        .then((responseJson) => {
            var projects = responseJson["object"]["projects"];
            var responseProjects = [];

            for (var index in projects) {
                responseProjects.push(new Project(projects[index]["name"], projects[index]["id"]))
            }

            callback(responseProjects);
        })
        .catch((error) => {
            console.error(error);
            callback(null);
        });
    }

    saveProject(project, callback) {
        fetch('http://localhost:8080/project/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: project.name
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
}
