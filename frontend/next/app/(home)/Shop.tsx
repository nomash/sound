import React from 'react'
import Card from "app/(shared)/TrackCard";
import Pagination from '../(shared)/Pagination';

interface Props {
    images: []
}

const Shop = ({ images } : Props) => {
    return (
        <section className="mt-10">
            <hr className="border-1" />
            <div className="flex items-center gap-3 my-8">
                <h4 className="bg-wh-900 py-2 px-5 text-wh-10  text-sm font-bold">
                SHOP
                </h4>
                <p className="font-bold text-2xl">No Mash Store</p>
            </div>

            <div className="sm:flex justify-between gap-20">
                <Card
                image={"download.jpeg"}
                className="basis-1/4 mt-5 sm:mt-0"
                imageHeight="h-80"
                />
                <Card
                image={"NoMash_22_NoShirtNoShoes_InstaPost_V2-01.png"}
                className="basis-1/4 mt-5 sm:mt-0"
                imageHeight="h-80"
                />
                <Card
                image={"NoMash_22_NoShirtNoShoes_InstaPost-01.png"}
                className="basis-1/4 mt-5 sm:mt-0"
                imageHeight="h-80"
                />
                <Card
                image={"NoMashSnowDay-Insta.png"}
                className="basis-1/4 mt-5 sm:mt-0"
                imageHeight="h-80"
                />
            </div>
            <div className="sm:flex justify-between gap-20">
                <Card
                image={"NoMash - Dapper Before Dust-01-IG.png"}
                className="basis-1/4 mt-5 sm:mt-0"
                imageHeight="h-80"
                />
                <Card
                image={"NoMash - Dapper Before Dust-01-IG.png"}
                className="basis-1/4 mt-5 sm:mt-0"
                imageHeight="h-80"
                />
                <Card
                image={"a1912853134_65.jpeg"}
                className="basis-1/4 mt-5 sm:mt-0"
                imageHeight="h-80"
                />
                <Card
                image={"NoMash_22_SlateAprilFool_IGPost.png"}
                className="basis-1/4 mt-5 sm:mt-0"
                imageHeight="h-80"
                />
            </div>
            <Pagination />
        </section>
    )
}

export default Shop
