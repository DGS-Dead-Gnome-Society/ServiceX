def run(self, target, channelName, nickname):
    self.partChannel(channelName, target, False)
    self.joinChannel(channelName, target, False)
