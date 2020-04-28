'use strict';

import React, {Component} from 'react';
import {
    StyleSheet,
    Text,
    View,
    Dimensions,
    TextInput,
} from 'react-native';
import Modal from 'react-native-modalbox';
import Button from 'react-native-button';
import {ServerProjectService} from '../Services/ServerProjectService.js';
import {Project} from '../Model/Project.js';

var screen = Dimensions.get('window');
export default class AddProjectModal extends Component {
    constructor(props) {
        super(props);
        this.state = {
            newProjectName: ''
        }
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
                <Text style={styles.modalTitle}>New project information</Text>
                <TextInput
                    style={styles.textInputSmall}
                    placeholder="Enter project name"
                    value = {this.state.newProjectName}
                    onChangeText={(text) => this.setState({newProjectName: text}) }
                />

                <Button
                    style={styles.saveButton}
                    containerStyle={styles.saveButtonContainer}
                    onPress={() => {
                        if(this.state.newProjectName.length == 0 ) {
                            alert("You must enter the name of the project.");
                            return;
                        }
                        var project = new Project(this.state.newProjectName);
                        var service = new ServerProjectService();
                        service.saveProject(project, (newId) => {
                            if (newId != null) {
                                project.id = newId
                                this.props.parentFlatList.addNewProject(project);
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
        height: 200,
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
