'use strict';

import React, {Component} from 'react';
import {
  StyleSheet,
  Text,
  View,
  FlatList,
  TouchableHighlight
} from 'react-native';
import {ServerProjectService} from '../Services/ServerProjectService.js';
import {MyStatusBar} from '../Misc/MyStatusBar.js';
import AddProjectModal from '../AddEditModals/AddProjectModal.js';

class ProjectListItem extends Component {

    constructor(props) {
        super(props);
        this.state = {
            activeRowKey: null
        };
    }

    render() {
    return (
        <View style={styles.listCell}>

            <View style = {styles.listItemTitleHolder}>
                <Text style={styles.listItemTitle}>{this.props.item.name}</Text>
            </View>

            <View style={styles.listSeparator}>

            </View>

        </View>);
    }
}

export default class ProjectListPage extends Component<{}> {
    constructor(props) {
        super(props);
        this.service = new ServerProjectService();
        this.state = ({
            projects: [],
        });
        this.onPressAdd = this.onPressAdd.bind(this);
        this.refreshList();
    }

    addNewProject(newProject) {
        var newProjects = this.state.projects;
        newProjects.push(newProject);
        console.log(newProjects);
        this.setState({projects: newProjects});
    }

    refreshList() {
        this.service.getProjects((receivedProjects) => {
            this.setState({projects: receivedProjects});
        })
    }

    onPressAdd() {
        this.refs.addModal.showAddModal();
    }

    render() {
        return(
            <View style={{flex: 1}}>
                <MyStatusBar backgroundColor="#4C4C4C" barStyle="light-content" />

                <View style={styles.listHeader}>

                    <View style = {styles.listHeaderBackButtonHolder}>
                    </View>

                    <View style = {styles.listHeaderTitleHolder}>
                        <Text style={styles.listHeaderTitle}> My Projects </Text>
                    </View>

                    <View style = {styles.listHeaderAddButtonHolder}>
                        <TouchableHighlight
                            style={styles.addButtonHolder}
                            onPress={this.onPressAdd}>
                            <Text style={styles.addButton}>Add</Text>
                        </TouchableHighlight>
                    </View>
                </View>

                <View style={styles.listHolder}>
                    <FlatList
                        ref = {'projectFlatList'}
                        data = {this.state.projects}
                        keyExtractor = {item => item.id.toString()}
                        renderItem={({item}) => {
                            return (
                                <ProjectListItem item={item} index={item.id} parentFlatList={this}>
                                </ProjectListItem>);
                            }}
                    />
                    <AddProjectModal ref={'addModal'} parentFlatList={this}>

                    </AddProjectModal>
                </View>
            </View>
        );
    }
}

const styles = StyleSheet.create({
    listHolder: {
        flex: 1,
        backgroundColor: 'rgb(120, 120, 120)',
    },
    listCell: {
        flex: 1,
        flexDirection: 'column',
        backgroundColor: 'rgb(120, 120, 120)',
        height: 60,
    },
    listItemTitleHolder: {
        flex: 1,
        height: 60,
        flexDirection: 'row',
        alignContent: 'center'
    },
    listItemTitle: {
        color: 'white',
        padding: 10,
        marginTop: 10,
        fontSize: 16,
    },
    listHeader: {
        backgroundColor: 'rgb(76, 76, 76)',
        height: 60,
        flexDirection: 'row',
    },
    listHeaderBackButtonHolder: {
        flex: 1,
        textAlign: 'left',
    },
    listHeaderTitleHolder: {
        flex: 1,
        textAlign: 'center',
        justifyContent: 'center',
        alignContent: 'center'
    },
    listHeaderAddButtonHolder: {
        flex: 1,
        textAlign: 'right',
        justifyContent: 'flex-end',
        alignContent: 'flex-end'
    },
    listHeaderTitle: {
        color: 'rgb(255,140,0)',
        fontSize: 20,
        alignSelf: 'center'
    },
    addButtonHolder: {
        height: 60,
        width: 60,
        marginRight: 10,
        padding: 10,
        alignSelf: 'flex-end',
        justifyContent: 'flex-end',
    },
    addButton: {
        flex: 1,
        color: 'rgb(255,140,0)',
        padding: 10,
        fontSize: 16,
    },
    listSeparator: {
        height: 1,
        backgroundColor: 'black'
    }
});
