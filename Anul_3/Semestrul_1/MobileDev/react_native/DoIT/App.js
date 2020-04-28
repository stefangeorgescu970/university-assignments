'use strict';

import React, {Component} from 'react';
import { createBottomTabNavigator } from 'react-navigation';
import ProjectListPage from './Classes/ListViews/MyProjectListPage.js';
import TaskListPage from './Classes/ListViews/TaskListPage.js';
import CompletedTaskListPage from './Classes/ListViews/CompletedTaskListPage.js';

export default createBottomTabNavigator({
    ToDo: TaskListPage,
    Done: CompletedTaskListPage,
    Projects: ProjectListPage
},
{
    tabBarOptions: {
        activeTintColor: 'rgb(255,140,0)',
        inactiveTintColor: 'white',
        activeBackgroundColor: 'rgb(76,76,76)',
        inactiveBackgroundColor: 'rgb(76,76,76)',
        style: {
            height: 50,
            backgroundColor: 'rgb(76,76,76)',
        },
        tabStyle: {
            height: 50,
            alignContent: 'center',
            justifyContent: 'center',
            showIcon: 'false'
        },
        labelStyle: {
            marginTop: 0,
            fontSize: 12,
        }
    }
});
