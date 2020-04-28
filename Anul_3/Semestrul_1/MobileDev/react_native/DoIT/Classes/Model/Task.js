'use strict';

export class Task {

    static makeid() {
        var text = "";
        var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

        for (var i = 0; i < 5; i++)
            text += possible.charAt(Math.floor(Math.random() * possible.length));

        return text;
    }

    constructor(name, description, dueDate, project, id) {
        if (id === undefined) {
            this.id = Task.makeid();
        } else {
            this.id = id
        }
        this.name = name;
        this.dueDate = dueDate;
        this.project = project;
        this.description = description;
        this.isCompleted = false;
        this.completedDate = null;
    }
}
