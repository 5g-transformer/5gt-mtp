/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mtp.extinterface.pa;

import com.google.common.eventbus.Subscribe;
import com.mtp.common.objects.LocalPAConfig;
import com.mtp.events.placement.PAComputeCall;
import com.mtp.events.placement.PAComputeConfig;
import com.mtp.events.placement.PANetworkCall;
import com.mtp.events.placement.PANetworkConfig;
import com.mtp.extinterface.pa.PAthreads.PAComputeRequestThreads;
import com.mtp.extinterface.pa.PAthreads.PANetworkRequestThread;

/**
 *
 * @author efabuba
 */
public class PlacementIF {
    
    private LocalPAConfig net_config;
    private LocalPAConfig comp_config;

    public PlacementIF() {
        net_config = null;
        comp_config = null;
    }
    
 //////////////////////EVENT-Handlers//////////////////////////////////////
    @Subscribe
    public void handle_PAComputeConfig (PAComputeConfig pacomp) {
        System.out.println("PlacementIF --> Handle PAComputeConfig Event");
        this.comp_config = pacomp.getComppaconfig();
    }
    
    @Subscribe
    public void handle_PANetworkConfig (PANetworkConfig panet) {
        System.out.println("PlacementIF --> Handle PANetworkConfig Event");
        this.net_config = panet.getNetpaconfig();
    }
    
    @Subscribe
    public void handle_PAComputeCall (PAComputeCall pacomp) {
        System.out.println("PlacementIF --> Handle PAComputeCall Event");
        ///Call Compute Thread
        PAComputeRequestThreads comp_thr = new PAComputeRequestThreads(comp_config, pacomp);
        comp_thr.run();
    }
    
    @Subscribe
    public void handle_PANetworkCall (PANetworkCall panet) {
        System.out.println("PlacementIF --> Handle PANetworkCall Event");
        //Call Network Thread
        PANetworkRequestThread net_thr = new PANetworkRequestThread(comp_config, panet);
        net_thr.run();
    }
}
