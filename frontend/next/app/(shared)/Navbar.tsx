import Link from 'node_modules/next/link'
import React from 'react'
import SocialLinks from './SocialLinks'

interface Props {
    
}

export const Navbar = (props: Props) => {
    return (
        <header className="mb-5">
            <nav className="flex justify-between items-center w-full bg-wh-900 text-wh-10 px-10 py-4">
                <div className="hidden sm:block">
                    <SocialLinks/>
                </div>
                <div className="flex justify-between items-center gap-20">
                    <Link href="/">Home</Link>
                    <Link href="/">About</Link>
                    <Link href="/">Tracks</Link>
                    <Link href="/">Shop</Link>
                </div>
                <div>
                    <p>Sign In</p>
                </div>
            </nav>
            <div className='flex justify-between gap-8 mt-5 mb-4 mx-10'>
                <div className="basis-2/3 md:mt-3">
                    <h1 className="font-bold text-3xl md:text-5xl">No Mash Sound</h1>
                    <p className="text-sm mt-3">
                        No Mash Sound Making SOUND
                    </p>
                </div>
                <div className="basis-full relative w-auto h-32 bg-wh-500">
                    My Image
                </div>
            </div>
            <hr className="border-1 mx-10"></hr>
        </header>
    )
}
