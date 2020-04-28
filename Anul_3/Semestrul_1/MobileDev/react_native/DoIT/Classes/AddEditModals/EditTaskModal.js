'use strict';

import React, {Component} from 'react';
import {
    StyleSheet,
    Text,
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
export default class EditTaskModal extends Component {
    constructor(props) {
        super(props);
        this.projectService = new ServerProjectService();
        this.taskService = new ServerTaskService();
        this.state = {
            key: '',
            flatListItem: null,
            taskName: '',
            taskDate: null,
            taskProject: null,
            selectedTaskProjectName: 'Choose Project',
            taskDescription: '',
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

    showEditModal(task, flatListItem) {
        this.setState({
            key: task.id,
            flatListItem: flatListItem,
            taskName: task.name,
            taskDate: new Date(task.dueDate),
            taskProject: task.project,
            taskDescription: task.description,
            selectedTaskProjectName: task.project.name
        })
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
                <Text style={styles.modalTitle}>Task information</Text>
                <TextInput
                    style={styles.textInputSmall}
                    placeholder="Task name"
                    value = {this.state.taskName}
                    onChangeText={(text) => this.setState({taskName: text}) }
                />

                <ModalDropdown
                    style={styles.projectDropdown}
                    options = {this.state.dropdownOptions}
                    defaultValue = {this.state.selectedTaskProjectName}
                    onSelect = {(value) => this.setState({newTaskProject: this.state.dropdownProjects[value]})}
                />

                <TextInput
                    style={styles.textInputSmall}
                    placeholder="Task description (optional)"
                    value = {this.state.taskDescription}
                    onChangeText={(text) => this.setState({taskDescription: text}) }
                />

                <Text style={styles.modalSubtitle}>Due date</Text>

                <DatePickerIOS
                    mode={'date'}
                    date={this.state.taskDate}
                    onDateChange={(date) => this.setState({taskDate: date})}
                />

                <Button
                    style={styles.saveButton}
                    containerStyle={styles.saveButtonContainer}
                    onPress={() => {
                        if(this.state.taskName.length == 0) {
                            alert("You must enter task name and project. Be careful to properly select the date.");
                            return;
                        }
                        var task = new Task(this.state.taskName, this.state.taskDescription, this.state.taskDate, this.state.taskProject)
                        this.taskService.update(this.state.key, task, (success) => {
                            if (success != false) {
                                this.state.flatListItem.refreshItem();
                            }
                        });
                        this.refs.myModal.close();
                    }}>
                    Save Updates
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
