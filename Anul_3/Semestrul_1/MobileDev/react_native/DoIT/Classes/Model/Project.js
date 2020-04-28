'use strict';

export class Project {

    static makeid() {
        var text = "";
        var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

        for (var i = 0; i < 5; i++)
            text += possible.charAt(Math.floor(Math.random() * possible.length));

        return text;
    }

    constructor(name, id) {
        if (id === undefined) {
            this.id = Project.makeid();
        } else {
            this.id = id
        }
        this.name = name
    }
}
