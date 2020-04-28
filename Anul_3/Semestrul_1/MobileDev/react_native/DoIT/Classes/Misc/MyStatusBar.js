'use strict';

import React, {Component} from 'react';
import {
    StyleSheet,
    View,
    StatusBar
} from 'react-native';

export const MyStatusBar = ({backgroundColor, ...props}) => (
  <View style={[styles.statusBar, { backgroundColor }]}>
    <StatusBar translucent backgroundColor={backgroundColor} {...props} />
  </View>
);

const styles = StyleSheet.create({
    statusBar: {
        height: 44,
    },
});
