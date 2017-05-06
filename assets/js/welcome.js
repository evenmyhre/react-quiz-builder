import React from 'react';

var Welcome = React.createClass({
    render: function() {
        return (

                    <div className="welcome-info">
                        <h1>Welcome to your Quiz Builder!</h1>
                        <h4>
                        This app is designed to be used as a study tool.  With it, you can enter questions under a specific 'topic'.
                        You are then able to take a test on a specific topic and receive summary results on how you did.
                        </h4>
                    </div>

        );
    }
});

export {Welcome};
