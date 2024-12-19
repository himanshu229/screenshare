import React from "react";
import { StyleSheet, View } from "react-native";
import ReactPlayer from "react-player";
function App() {
  return (
    <View style={styles.container}>
      <ReactPlayer
        url="http://<laptop-ip>:5000/screen" // Replace <laptop-ip> with your actual IP
        width="100%" // Make the video full width
        height="100%" // Make the video full height
        controls={true} // Optional: Add video controls
        playing={true} // Optional: Auto-play the video
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    position: "relative",
    width: "100%",
    height: "100vh", // Full viewport height
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
  },
});

export default App;
