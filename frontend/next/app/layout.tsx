import './globals.css'
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import {Navbar} from "app/(shared)/Navbar"
import Footer from "app/(shared)/Footer"

const inter = Inter({ subsets: ['latin'] })


// export const metadata: Metadata = {
//   title: 'NoMashSound',
//   description: 'No Mash Sound e-commerce site',
// }

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className={inter.className}>
        <Navbar/>
        {children}
        <Footer/>
    </div>
  )
}
