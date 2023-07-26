import React from 'react'


const Footer = () => {
    return (
        <footer className="bg-wh-900 text-wh-50 py-10 px-10">
            <div className="justify-between mx-auto gap-16 sm:flex">
                {}
                <div className="mt-16 basis-1/2 sm:mt-0">
                    <h4 className="font-bold"></h4>
                    <p className="my-5">
                        random text
                    </p>
                    <p>
                        No Mash Sound All Rights Reserved
                    </p>
                </div>
                <div className="mt-16 basis-1/4 sm:mt-0">
                    <h4 className="font-bold">Links</h4>
                    <p className="my-5"> SOMETHING </p>
                    <p className="my-5"> Some random link again </p>
                    
                </div>
                <div className="mt-16 basis-1/4 sm:mt-0">
                    <h4 className="font-bold">Contact Us</h4>
                    <p className="my-5"> No Mash </p>
                    <p className="my-5"> nomashrecords@gmail.com </p>
                    
                </div>
            </div>
        </footer>
    )
}

export default Footer
