import React from 'react'
import TrackCard from "@/app/(shared)/TrackCard"
import Pagination from '../(shared)/Pagination'

interface Props {
    data: string
}

const Tracks = ({data}: Props) => {

    return (
        <section className="mt-10">
            <hr className="border-1" />
            <div className="flex items-center gap-3 my-8">
                <h4 className="bg-accent-orange py-2 px-5 text-wh-900 text-sm font-bold">
                    TRACKS
                </h4>
                <p className="font-bold text-2xl">Hottest Tracks of the Month</p>
            </div>

            <div className="sm:grid grid-cols-2 grid-rows-3 gap-x-8 gap-y-8 my-5">
                <TrackCard image={"download.jpeg"} imageHeight="h-96" isLongForm className="col-span-1 row-span-3"></TrackCard>
                <TrackCard image={"a1912853134_65.jpeg"} imageHeight="h-48" isSmallCard className="col-span-1 row-span-1 mt-10 sm:mt-0 flex justify-between gap-3"/>
                <TrackCard image={"martinbutt.jpeg"} imageHeight="h-48" isSmallCard className="col-span-1 row-span-1 mt-10 sm:mt-0 flex justify-between gap-3"/>
                <TrackCard image={"a1912853134_65.jpeg"} imageHeight="h-48" isSmallCard className="col-span-1 row-span-1 mt-10 sm:mt-0 flex justify-between gap-3"/>

                
            </div>
            <Pagination />

        </section>
    )
}

export default Tracks
