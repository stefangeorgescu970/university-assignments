'use strict';

import React, {Component} from 'react';
import {
    StyleSheet,
    Text,
    View,
    Alert,
    Dimensions,
    TextInput,
    DatePickerIOS,
} from 'react-native';
import Modal from 'react-native-modalbox';
import Button from 'react-native-button';
import ModalDropdown from 'react-native-modal-dropdown';
import {ServerTaskService} from '../Services/ServerTaskService.js';
import {ServerProjectService} from '../Services/ServerProjectService.js'
import {Task} from '../Model/Task.js'

var screen = Dimensions.get('window');
export default class AddTaskModal extends Component {

    constructor(props) {
        super(props);
        this.projectService = new ServerProjectService();
        this.state = {
            newTaskName: '',
            newTaskDate: new Date(),
            newTaskProject: null,
            newTaskDescription: '',
            dropdownProjects: null,
            dropdownOptions: null
        }

        this.projectService.getProjects((receivedProjects) => {
            this.setState({
                dropdownProjects: receivedProjects,
                dropdownOptions: receivedProjects.map(function(item) {return item.name}),
            });
        })
    }

    refreshList() {
        this.projectService.getProjects((receivedProjects) => {
            this.setState({
                dropdownProjects: receivedProjects,
                dropdownOptions: receivedProjects.map(function(item) {return item.name}),
            });
        })
    }

    showAddModal() {
        this.refs.myModal.open();
    }

    render() {
        return (
            <Modal
            ref={"myModal"}
            style={styles.addModal}
            position='center'
            backdrop={true}
            onClosed={() => {

            }}
            >
                <Text style={styles.modalTitle}>New task information</Text>
                <TextInput
                    style={styles.textInputSmall}
                    placeholder="Enter task name"
                    value = {this.state.newTaskName}
                    onChangeText={(text) => this.setState({newTaskName: text}) }
                />

                <ModalDropdown
                    style={styles.projectDropdown}
                    options = {this.state.dropdownOptions}
                    defaultValue = {'Choose Project'}
                    onSelect = {(value) => this.setState({newTaskProject: this.state.dropdownProjects[value]})}
                />

                <TextInput
                    style={styles.textInputSmall}
                    placeholder="Enter task description (optional)"
                    value = {this.state.newTaskDescription}
                    onChangeText={(text) => this.setState({newTaskDescription: text}) }
                />

                <Text style={styles.modalSubtitle}>Choose due date</Text>

                <DatePickerIOS
                    mode={'date'}
                    date={this.state.newTaskDate}
                    onDateChange={(date) => this.setState({newTaskDate: date})}
                />

                <Button
                    style={styles.saveButton}
                    containerStyle={styles.saveButtonContainer}
                    onPress={() => {
                        if(this.state.newTaskName.length == 0 || this.state.newTaskProject == null) {
                            alert("You must enter task name and project. Be careful to properly select the date.");
                            return;
                        }
                        var task = new Task(this.state.newTaskName, this.state.newTaskDescription, this.state.newTaskDate, this.state.newTaskProject, -1)
                        console.log(task.id);
                        var service = new ServerTaskService();
                        service.saveTask(task, (newId) => {
                            if (newId != null) {
                                task.id = newId;
                                this.props.parentFlatList.addNewTask(task);
                            }
                        });
                        this.refs.myModal.close();
                    }}>
                    Save
                </Button>
            </Modal>
        );
    }
}

const styles = StyleSheet.create({
    description: {
        fontSize: 20,
        textAlign: 'center',
        color: '#656565',
        marginTop: 200,
        flex: 1,
    },
    container: {
        flex: 1,
    },
    addModal: {
        justifyContent: 'center',
        borderRadius: 20,
        shadowRadius: 20,
        width: screen.width - 80,
        height: 550,
    },
    modalTitle: {
        fontSize: 16,
        fontWeight: 'bold',
        textAlign: 'center',
        marginTop: -10,
  },
  modalSubtitle: {
      fontSize: 14,
      fontWeight: 'bold',
      textAlign: 'center',
      marginTop: 10,
      },
    textInputSmall: {
        height: 40,
        borderBottomColor: 'gray',
        marginLeft: 30,
        marginRight: 30,
        marginTop: 20,
        marginBottom: 10,
        borderBottomWidth: 1,
    },
    saveButton: {
        fontSize: 18,
        color: 'white',
    },
    saveButtonContainer: {
        padding: 8,
        marginLeft: 70,
        marginRight: 70,
        height: 40,
        borderRadius: 6,
        backgroundColor: 'gray',
    },
    projectDropdown: {
        height: 40,
        borderBottomColor: 'gray',
        marginLeft: 30,
        marginRight: 30,
        marginTop: 20,
        marginBottom: 10,
        borderBottomWidth: 1,
    },
});
